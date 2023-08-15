from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        number0 = 0
        number1 = 0
        number2 = 0
        for i in nums:
            if i == 0:
                number0 += 1
            elif i == 1:
                number1 += 1
            else:
                number2 += 1
        nums[:] = number0*[0] + number1*[1] + number2*[2]