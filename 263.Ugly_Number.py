class Solution:
    def isUgly(self, n: int) -> bool:
        while n%2 == 0:
            n //= 2
            if n == 0:
                break
        while n%3 ==0:
            n //= 3
            if n == 0:
                break
        while n%5 ==0:
            n //= 5
            if n == 0:
                break
        if n == 1:
            return True
        return False