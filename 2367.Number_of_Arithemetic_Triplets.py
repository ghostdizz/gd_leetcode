from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        dic = {}
        quest = {}
        count = 0
        for i in nums:
            dic[i] = True
            if i in quest:
                count += 1
            if i - diff in dic:
                quest[i+ diff] = True
        return count