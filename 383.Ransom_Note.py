class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lst = list(magazine)
        for i in ransomNote:
            if i in lst:
                lst.remove(i)
            else:
                return False
        return True
            