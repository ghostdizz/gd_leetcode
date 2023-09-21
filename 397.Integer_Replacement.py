class Solution:
    def __init__(self):
        self.min_count = float('inf')

    def recursion(self, n, count):
        if count >= self.min_count:
            return
        if n == 1: 
            if count < self.min_count:
                self.min_count = count
            return
        if n%2 == 0:
            self.recursion(n//2, count + 1)
        else:
            self.recursion(n+1, count + 1)
            self.recursion(n-1, count + 1)

    def integerReplacement(self, n: int) -> int:
        self.recursion(n, 0)
        return self.min_count
    
