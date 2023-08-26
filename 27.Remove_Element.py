from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        
        i = 0
        while i < k:
            if nums[i] == val:
                k -= 1
                nums.pop(i)
            else:
                i += 1
        return k