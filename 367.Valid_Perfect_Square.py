class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(num**(1/2))**2 == num
    
