from typing import List

class Solution:
    def __init__(self):
        self.lst = []
    
    def combination(self, candidates: list, idx: int, nums: list, target: int) -> bool:
        if target < 0: return
        if target == 0: 
            self.lst.append(nums)
            return
        while idx < len(candidates):
            if (target - candidates[idx]) >= 0:
                self.combination(candidates, idx, nums + [candidates[idx]], target - candidates[idx])
            idx += 1
        return 

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combination(candidates, 0, [], target)
        return self.lst
    