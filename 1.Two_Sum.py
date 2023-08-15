from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, e in enumerate(nums):
            if e in dic:
                return i, dic[e]
            else:
                dic[target-e] = i