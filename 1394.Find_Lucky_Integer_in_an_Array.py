from typing import List
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        my_dict = {}
        lucky_number = -1
        for i  in arr:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        for j in my_dict:
            if j == my_dict[j] and j>lucky_number:
                lucky_number = j
        return lucky_number

