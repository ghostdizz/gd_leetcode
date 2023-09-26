from typing import List

class Solution:
    def __init__(self):
        self.my_dict = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}
        self.lst = []

    def combinate(self, digits, string):
        if digits == "": 
            self.lst.append(string)
            return
        for i in self.my_dict[int(digits[0])]:
            self.combinate(digits[1:], string+i)

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        self.combinate(digits, "")
        return self.lst
