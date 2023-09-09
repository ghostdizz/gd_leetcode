from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}
        
        for i in range(len(numbers)):
            if (target-numbers[i]) in my_dict:
                return [my_dict[target-numbers[i]]+1, i+1]
            else:
                my_dict[numbers[i]] = i