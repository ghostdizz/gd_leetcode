from typing import List
from collections import OrderedDict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        prev_val = None
        for i in nums:
            if i != prev_val:
                prev_val = i
                count += 1
        nums[:] = list(OrderedDict.fromkeys(nums))
        return count
    
    