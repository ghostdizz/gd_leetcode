from math import ceil

class Solution:
    def __init__(self):
        self.s = ""
    def factorial(self, n):
        if n==1 or n==0:
            return n
        return n*self.factorial(n-1)
    
    def recursion(self, Set, length, k, fac):
        if length == 1:
            self.s += str(list(Set)[0])
            return 0
        self.s += str(list(Set)[ceil(k/fac)-1])
        Set.remove(list(Set)[ceil(k/fac)-1])
        
        self.recursion(Set, length-1, k%(fac), fac//(length-1))
        
    def getPermutation(self, n: int, k: int) -> str:
        fac = self.factorial(n-1)
        Set = set([i for i in range(1,n+1)])
        self.recursion(Set, n, k, fac)
        return self.s