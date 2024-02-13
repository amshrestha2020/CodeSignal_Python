class ReferenceCounter:
    """ Tracks the number of duplications to a particular
        address in the storage system.
        The first time unique data is written, a new ReferenceCounter instance
        is created with refs == 1. Then each
        subsequent duplicate write or delete will increment or decrement refs.
        When there are no more references to the address (refs = 0),
        the ReferenceCounter object should be discarded.
    """
    def __init__(self, addr, refs):
        """
        addr: integer index into a StorageArray's data_storage
        refs: integer number of duplicate writes to addr
        """
        self.addr = addr
        self.refs = refs


class StorageArray:
    """ Basic implementation of an in-memory storage system
        represented by an array. A lookaside hashtable tracks the
        ReferenceCounters for duplicated data within the data_storage.
        This basic storage system only supports three operations:
            - write data to next available address;
            - read data from specified address;
            - delete data from specified address.
    """

    def __init__(self):
        """ data_storage: array of data objects of length 64
            alloc_addr_ptr: integer of the last allocated index
            dedup_lookaside: hashtable containing ReferenceCounters
                            to track writes of duplicate data
        """
        self.data_storage = [None] * 64
        self.alloc_addr_ptr = 0
        self.dedup_lookaside = {}

    def _alloc_addr(self):
        """ Internal method that grabs the next available free
            address in the data_storage (i.e., address that does
            not point to data with a corresponding ReferenceCounter
            entry in the dedup_lookaside)

            returns: integer addr to use for the next write operation
                or None if no free addr is available
        """
        start_alloc_addr_ptr = self.alloc_addr_ptr
        while True:
            ref_counter = self.dedup_lookaside.get(self.data_storage[self.alloc_addr_ptr])
            if ref_counter is None or ref_counter.addr != self.alloc_addr_ptr:
                break
            self.alloc_addr_ptr = (self.alloc_addr_ptr + 1) % len(self.data_storage)
            if self.alloc_addr_ptr == start_alloc_addr_ptr:
                # No free address available
                return None

        return self.alloc_addr_ptr

    def write(self, data):
        """ Takes in a data object and stores it in the data_storage.
            If the data duplicates to existing data, write() increments
            the reference count instead of allocating a new address. If
            the data is unique (i.e., does not have a corresponding
            ReferenceCounter entry in the dedup_lookaside), but there
            are not any available addresses, return the sentinel value
            of None to signify the write failed.

            data: string to store in the data_storage or record
                duplicate of
            returns: integer addr where the data is stored
                or None if space was required but not available
        """

        # Check if the data is already present in the storage
        if data in self.dedup_lookaside:
            ref_counter = self.dedup_lookaside[data]
            ref_counter.refs += 1
            return ref_counter.addr

        # Try to find a free address
        addr = self._alloc_addr()
        if addr is None:
            return None

        # Write data to the found address
        self.data_storage[addr] = data
        self.dedup_lookaside[data] = ReferenceCounter(addr, 1)
        self.alloc_addr_ptr = (addr + 1) % len(self.data_storage)
        return addr


    def read(self, addr):
        """ Takes in an integer address and retrieves the data at the
            location in the data_storage, only if there are still
            references to the data. If there are no references (i.e.,
            does not point to data with a corresponding ReferenceCounter
            entry in the dedup_lookaside), then return the sentinel
            value None to signify the address is unused or the data has
            been deleted.

            addr: integer address where the data is stored
            returns: object retrieved from data_storage at addr
                or None if there are no references on the data
                at the address
        """

        if addr < 0 or addr >= len(self.data_storage):
            return None

        data = self.data_storage[addr]
        ref_counter = self.dedup_lookaside.get(data)
        if ref_counter is None or ref_counter.addr != addr:
            return None

        return data
        
    def delete(self, addr):
        """ Takes in an integer address and deletes the data at the
            location in the data_storage by decrementing the reference
            count of the data's corresponding ReferenceCounter in the
            dedup_lookaside. If the delete would decrement the count to
            0, remove the ReferenceCounter from the dedup_lookaside.

            addr: integer address where the data is stored
            returns: data stored in the address or None if there isn't any
        """

        if addr < 0 or addr >= len(self.data_storage):
            return None

        data = self.data_storage[addr]
        ref_counter = self.dedup_lookaside.get(data)
        if ref_counter is None or ref_counter.addr != addr:
            return None

        ref_counter.refs -= 1
        if ref_counter.refs == 0:
            del self.dedup_lookaside[data]
            # Check if the deleted data was the last entry at the current address
            if addr == self.alloc_addr_ptr:
                # Find the next available address
                while self.alloc_addr_ptr < len(self.data_storage):
                    if self.data_storage[self.alloc_addr_ptr] not in self.dedup_lookaside:
                        break
                    self.alloc_addr_ptr += 1
                # Reset the address pointer to the beginning if no free address is found
                if self.alloc_addr_ptr >= len(self.data_storage):
                    self.alloc_addr_ptr = 0

        return data
    
def solution(operations):
    ans = []
    dataStorage = StorageArray()
    for operation in operations:
        if operation.startswith('READ '):
            ans.append(str(dataStorage.read(int(operation[5::]))))
        elif operation.startswith('WRITE '):
            ans.append(str(dataStorage.write(operation[6::])))
        elif operation.startswith('DELETE '):
            ans.append(str(dataStorage.delete(int(operation[7::]))))
    return ans
