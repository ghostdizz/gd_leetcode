from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        my_dict = {}
        lst = []
        for i in nums1:
            my_dict[i] = False
        for j in nums2:
            if j in my_dict:
                lst.append(j)
        return lst