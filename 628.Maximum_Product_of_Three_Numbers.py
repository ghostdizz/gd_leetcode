from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-3]*nums[-2]*nums[-1]
        if nums[0]*nums[1]*nums[-1] > a:
            return nums[0]*nums[1]*nums[-1]
        return a
