class Prizes(object):
    def __init__(self, purchases, n, d):
        self.purchases = purchases
        self.n = n
        self.d = d
        self.i = n - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.purchases):
            i = self.i
            self.i += self.n
            if self.purchases[i] % self.d == 0:
                return i + 1
        raise StopIteration

def solution(purchases, n, d):
    return list(Prizes(purchases, n, d))
    