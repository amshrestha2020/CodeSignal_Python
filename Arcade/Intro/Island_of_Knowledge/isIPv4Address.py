def solution(inputString):
    parts = inputString.split('.')
    
    # Check if there are exactly four parts
    if len(parts) != 4:
        return False
    
    for part in parts:
        # Check if each part is a valid integer
        if not part.isdigit():
            return False

        # Check if each number is in the range [0, 255]
        if not (0 <= int(part) <= 255):
            return False

    # Check if the original string starts and ends with a digit
    if not inputString.split('.')[0].isdigit() or not inputString.split('.')[-1].isdigit():
        return False
    
    # Check if the original string and each part have the same representation
    if inputString != '.'.join(str(int(part)) for part in parts):
        return False
    return True

