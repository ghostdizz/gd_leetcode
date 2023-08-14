from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k%length
        if k == 0:
            return 0
        else:
            nums[:] = nums[-k:] + nums[:(length-k)]