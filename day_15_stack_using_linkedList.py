class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, data):
        node = Node(data)
        if (self.top == None):
            self.top = node
            return
        
        node.next = self.top
        self.top = node
    
    def pop(self):
        if (self.top == None):
            raise Exception('Stack is empty!!')
        
        temp = self.top
        self.top = self.top.next
        return temp

    def print(self):
        temp = self.top
        if (temp == None):
            print('Stack is Empty!!!!!!,  Go ahead and do some push operation first......')
            return
        while (temp):
            print(temp.data, end= ' ')
            temp = temp.next
        print('\n')
    


if __name__ == "__main__":
    print('Hello Developers!!!')

    stack = Stack()
    stack.push(1); stack.push(2); stack.push(3); stack.push(4); stack.push(5);
    stack.print()
    stack.pop()
    stack.print()
    stack.pop(); stack.pop(); stack.pop(); stack.pop(); #stack.pop();
    stack.print()