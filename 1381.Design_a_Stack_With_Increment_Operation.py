class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.length = 0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.length < self.maxSize:
            self.stack.append(x)
            self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            return -1
        self.length -= 1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(self.length, k)):
            self.stack[i] += val
    
