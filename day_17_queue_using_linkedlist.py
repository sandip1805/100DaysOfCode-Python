class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        node = Node(data)
        if(self.front == None and self.rear == None):
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node
        self.print()
    
    def dequeue(self):
        if (self.front == None and self.rear == None):
            print("Queue is empty, nothing to dequeue!!!!!")
        elif(self.front == self.rear):
            temp = self.front.data
            self.front = self.rear = None
            self.print()
            return temp
        else:
            temp = self.front.next
            self.front = self.front.next
            self.print()
            return temp.data
    
    def print(self):
        temp = self.front
        while(temp):
            print(f'{temp.data}', end=' ')
            temp = temp.next
        print('\n')

if __name__ == "__main__":
    print('Queue implementation using LinkedList')
    queue = Queue()
    for i in range(0, 10):
        queue.enqueue(i)        
    for i in range(0, 10):
        queue.dequeue()        
    queue.dequeue()
        



