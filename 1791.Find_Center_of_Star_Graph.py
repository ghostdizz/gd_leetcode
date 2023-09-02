from collections import Counter
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        lst = [i for j in edges[0:2] for i in j]
        c = Counter(lst)
        max_value = max(c.values())
        for key, value in c.items():
            if value == max_value:
                return key
        return -1