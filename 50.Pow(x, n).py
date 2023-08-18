class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n>0:
            return x*self.myPow(x, n-1)
        elif n<0:
            return (1/x)*self.myPow(x, n+1)
