class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp_var = 0
        y = x
        while y != 0:
            temp_var = temp_var*10 + y%10
            y //= 10
        if temp_var == x:
            return True
        return False
    