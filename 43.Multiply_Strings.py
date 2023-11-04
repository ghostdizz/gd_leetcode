class Solution:
    def convert_string_to_integer(self, n):
        ans = 0
        for i in n:
            ans = ans*10 + ord(i)-48
        return ans
    
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.convert_string_to_integer(num1) * self.convert_string_to_integer(num2))
    
