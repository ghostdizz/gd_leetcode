from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def permutation(arr1, arr2):
            if len(arr2) == 0:
                ans.append(arr1)
            else:
                for i in range(len(arr2)):
                    permutation(arr1+[arr2[i]], arr2[:i] + arr2[(i+1):])
        
        permutation([], nums)
        return ans
