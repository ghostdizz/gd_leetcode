from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        my_dict = {}
        
        ans = []
        for i in nums:
            my_dict[i] = True
        for j in range(1, length+1):
            if j not in my_dict:
                ans.append(j)
        return ans
    