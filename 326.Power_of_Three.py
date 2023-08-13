class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        elif n%3 == 0:
            return True and self.isPowerOfThree(n//3)
        return False
