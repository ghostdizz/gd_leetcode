from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums = sorted(nums1)
        length = len(nums)
        if length%2 == 0:
            a = int((length-1)/2)
            return (nums[a] + nums[a+1])/2
        else:
            return nums[int((length-1)/2)]
print(Solution().findMedianSortedArrays([1,3], [2]))