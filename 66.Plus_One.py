from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = [str(integer) for integer in digits]
        a_string = "".join(strings)
        an_integer = str(int(a_string) + 1)
        arr = [int(_) for _ in an_integer]
        return arr
        
        