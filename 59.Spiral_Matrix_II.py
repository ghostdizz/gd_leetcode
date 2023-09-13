from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        lst = [[None]*n for _ in range(n)]
        num = 1
        horizontal1 = 0
        horizontal2 = n-1
        vertical1 = 0
        vertical2 = n-1
        while horizontal2 >= horizontal1 and vertical2 >= vertical1:
            for i in range(vertical1, vertical2+1):
                lst[horizontal1][i] = num
                num += 1
            horizontal1 += 1
            for i in range(horizontal1, horizontal2+1):
                lst[i][vertical2] = num
                num += 1
            vertical2 -= 1

   
            for i in range(vertical2, vertical1-1, -1):
                lst[horizontal2][i] = num
                num += 1
            horizontal2 -= 1
         
            for i in range(horizontal2, horizontal1-1, -1):
                lst[i][vertical1] = num
                num += 1
            vertical1 += 1
        return lst
    
