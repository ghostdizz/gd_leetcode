from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def permute(arr1, arr2):
            if len(arr2) == 0:
                ans.append(arr1)
            else:
                for i in range(len(arr2)):
                    if i > 0 and arr2[i] == arr2[i-1]:
                        continue
                    permute(arr1+[arr2[i]], arr2[:i]+arr2[(i+1):])

        nums.sort()
        permute([], nums)
        return ans
    
