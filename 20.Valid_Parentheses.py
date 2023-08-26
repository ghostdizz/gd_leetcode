class Stack:
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return self.__len__() == 0
    def top(self):
        if self.is_empty():
            print("Stack is empty!")
        return self.data[-1]
    def push(self, n):
        self.data.append(n)
    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
        return self.data.pop()
    
class Solution:
    def isValid(self, s: str) -> bool:
        dct = {")":"(", "]":"[", "}":"{", "(":"a", "[":"b","{":"c"}
        stack = Stack()
        stack.push(0)
        for i in s:
            if dct[i] == stack.top():
                stack.pop()
            else:
                stack.push(i)
        if stack.__len__() == 1:
            return True
        else:
            return False
        
