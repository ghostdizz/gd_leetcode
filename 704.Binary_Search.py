from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx1 = 0
        idx2 = len(nums)-1
        if idx1 == idx2:
            if nums[0] == target:
                return 0
            else:
                return -1
        mid = (idx1+idx2)//2
        while idx1 != idx2-1:
            if target >= nums[mid]:
                idx1 = mid
            else:
                idx2 = mid
            mid = (idx1+idx2)//2
        if nums[idx1] == target:
            return idx1
        elif nums[idx2] == target:
            return idx2
        return -1

        