class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for index in range(len(s)):
            s[index] = s[index][::-1]
        
        return ' '.join(s)
