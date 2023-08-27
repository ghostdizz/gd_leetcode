class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(map(str, s.split()[::-1]))

