from typing import List
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from empty stack")

    def size(self):
        return len(self.items)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = Stack()
        for i in tokens:
            if i == "+":
                stack.push(stack.pop() + stack.pop())
            elif i == "-":
                var2 = stack.pop()
                var1 = stack.pop()
                stack.push(var1 - var2)
            elif i == "*":
                stack.push(stack.pop() * stack.pop())
        
            elif i == "/":
                var2 = stack.pop()
                var1 = stack.pop()
                stack.push(int(var1/var2))
            else:
                stack.push(int(i))
        return stack.peek()

