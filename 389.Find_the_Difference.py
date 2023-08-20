from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count1 = Counter(s)
        count2 = Counter(t)
        for i in count2:
            try:
                if count2[i] > count1[i]:
                    return i
            except:
                if i not in count2:
                    return i

