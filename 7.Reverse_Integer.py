class Solution:
    def reverse(self, x: int) -> int:        
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = abs(x)
            x = - int(str(x)[::-1])
        if x < -2**31 or x > 2**31 -1:
            return 0
        return x