class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1 = len(word1)
        length2 = len(word2)
        
        s = ""
        for i in range(min(length1, length2)):
            s += word1[i] + word2[i]
        if length1 < length2:
            s += word2[length1:]
        elif length1 > length2:
            s += word1[length2:]
        return s
