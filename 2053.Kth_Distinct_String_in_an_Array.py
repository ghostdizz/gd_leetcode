from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        my_dict = {}
        for i in arr:
            if i in my_dict:
                my_dict[i] += 1
                continue
            my_dict[i] = 1
        idx = 0
        for j in my_dict:
            if my_dict[j] == 1:
                if idx == k-1:
                    return j
                idx += 1
        return ""
