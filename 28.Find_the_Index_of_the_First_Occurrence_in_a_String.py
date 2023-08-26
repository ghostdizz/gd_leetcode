class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle != "":
            return -1
        elif haystack == "" and needle == "":
            return 0
        else:
            return haystack.find(needle)