class Stack:
    def __init__(self) -> None:
        self.maxSize = 100
        self.data = [None] * self.maxSize
        self.top = -1
    
    def push(self, data):
        if (self.top == self.maxSize-1):
            raise Exception("Stack overflow!")
        self.top += 1        
        self.data[self.top] = data
    
    def pop(self):
        if (self.top == -1):
            raise Exception("Stack is empty")
        item = self.data[self.top]
        self.top -= 1
        return item
    
    def top(self):
        if (self.top == -1):
            raise Exception("Stack is empty")
        return self.data[self.top]
    
    def printStack(self):
        print(self.data)

if __name__ == '__main__':
    stack = Stack()
    for i in range(0, 99):
        stack.push(i)
    stack.push(1)
    stack.printStack()