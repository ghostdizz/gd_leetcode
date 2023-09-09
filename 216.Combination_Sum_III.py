from typing import List

class Solution:
    def __init__(self):
        self.lst = []
    def combinate(self, i: int, nums: List[int], k: int, n: int):
        if n < 0: return
        if len(nums) == k:
            if n == 0:
                self.lst.append(nums)
            return
        for i in range(i, 10):
            self.combinate(i+1, nums + [i], k, n-i)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.combinate(1, [], k, n)
        return self.lst
    
