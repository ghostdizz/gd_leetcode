from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        my_dict = {}
        for path in paths:
            my_dict[path[0]] = True
        for path1 in paths:
            if path1[1] not in my_dict:
                return path1[1]
        