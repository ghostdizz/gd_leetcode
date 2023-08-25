from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = [0] * k

        def recursion(position, current):
            if position == k:
                ans.append(nums[:])
                return 0
            for i in range(current, n-k+position+2):
                nums[position] = i
                recursion(position+1, i+1)
        
        recursion(0, 1)
        return ans
    
