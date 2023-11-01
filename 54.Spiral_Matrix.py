from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        horizontal1, horizontal2 = 0, len(matrix)-1
        vertical1, vertical2 = 0, len(matrix[0])-1
        length = 0
        length_matrix = (vertical2+1)*(horizontal2+1)
        arr = []
        while length < length_matrix:
            for i in range(vertical1, vertical2+1):
                arr.append(matrix[horizontal1][i])
                length += 1
            horizontal1 += 1
            for i in range(horizontal1, horizontal2+1):
                arr.append(matrix[i][vertical2])
                length += 1
            vertical2 -= 1
            if horizontal1 <= horizontal2:
                for i in range(vertical2, vertical1-1, -1):
                    arr.append(matrix[horizontal2][i])
                    length += 1
                horizontal2 -= 1
            if vertical1 <= vertical2:
                for i in range(horizontal2, horizontal1-1, -1):
                    arr.append(matrix[i][vertical1])
                    length += 1
                vertical1 += 1
        return arr