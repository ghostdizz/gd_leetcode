class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            return self.check(n)
    def check(self, n):
        if n == 1:
            return True
        elif n%4 == 0:
            return True and self.isPowerOfFour(n//4)
        return False
