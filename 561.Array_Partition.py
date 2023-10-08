from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            s += nums[i]
        return s