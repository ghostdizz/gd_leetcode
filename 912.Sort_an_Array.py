from typing import List

class Solution:
    def merge(self, a: List[int], b: List[int]):
        c = []
        while len(a) != 0 and len(b) != 0:
            if a[0] >= b[0] :
                c.append(b.pop(0))
            else:
                c.append(a.pop(0))        
        while len(a) != 0:
            c.append(a.pop(0))
        while len(b) != 0:
            c.append(b.pop(0))
        return c
    
    def merge_sort(self, arr: List[int]):
        if len(arr) == 1:
            return arr
        arr1 = [arr[i] for i in range(0, int(len(arr)/2))]
        arr2 = [arr[i] for i in range(int(len(arr)/2), len(arr))]
        arr1 = self.merge_sort(arr1)
        arr2 = self.merge_sort(arr2)
        return self.merge(arr1, arr2)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)



    