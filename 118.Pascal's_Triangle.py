from typing import List
from math import comb
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []
        for i in range(numRows):
            temp_lst = [comb(i, j) for j in range(i+1)]
            lst.append(temp_lst)
        
        return lst
    
