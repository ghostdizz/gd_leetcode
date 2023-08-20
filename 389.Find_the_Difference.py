class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for i in s:
            dic[i] = True
        for j in t:
            if j not in dic:
                return j
            