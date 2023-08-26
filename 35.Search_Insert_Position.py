from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return n
        