from typing import List

class Solution:
    def convertListToString(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        else:
            return str(nums[0]) + "->" + str(nums[-1])
        
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        lst = []
        pre_num = None
        for i in range(len(nums)):
            if len(lst) == 0 or pre_num+1 == nums[i]:
                lst.append(nums[i])
            else:
                ans.append(self.convertListToString(lst))
                lst = [nums[i]]
            pre_num = nums[i]
        if lst != []:
            ans.append(self.convertListToString(lst))
        return ans
    

