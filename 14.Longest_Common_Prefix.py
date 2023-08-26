from typing import List

class Solution:    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_lenght = self.findTheShortestString(strs)
        result = ""
        for i in range(shortest_lenght):
            boolean = True
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    boolean = False
                    break
            if boolean == True:
                result += strs[0][i]
            else:
                break
        return result  
    
    def findTheShortestString(self, s):
        return len(min(s, key=len))