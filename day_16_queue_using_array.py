class Queue:
    def __init__(self, size) -> None:
        self.size = size
        self.data = [None] * size
        self.front = -1
        self.rear = -1
    
    # Helper function to check if queue is full or not
    def isFull(self):
        return ((self.rear + 1) % self.size == self.front)
    
    def print(self):
        print(f'Queue: {self.data}')

    def isEmpty(self):
        return (self.front == -1 and self.rear == -1)

    def enqueue(self, data):
        if self.isFull():
            print('Queue is Full')
        elif(self.front == -1):
            self.front = self.rear = 0
            self.data[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.data[self.rear] = data

    def dequeue(self):
        if (self.isEmpty()):
            print("Queue is Empty!!")
        elif(self.front == self.rear):
            d = self.data[self.front]
            self.data[self.front] = None
            self.front = self.rear = -1
            return d
        else:
            d = self.data[self.front]
            self.data[self.front] = None
            self.front = (self.front + 1) % self.size
            return d
            

if __name__ == "__main__":
    queue = Queue(5)
    queue.enqueue(10); queue.enqueue(11); queue.enqueue(12); 
    queue.print()
    queue.dequeue(); queue.enqueue(13); queue.dequeue();  queue.dequeue();  queue.dequeue();  queue.dequeue();     
    queue.print()
    queue.enqueue(10); queue.enqueue(11); queue.enqueue(12); 
    queue.print()