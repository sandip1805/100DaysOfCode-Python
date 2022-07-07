#Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data) -> None:
        self.data = data # Assign data to instance variable
        self.next = None # initialize next with none/null
        self.prev = None # Initialize prev with None/null

class DoublyLinkedList:
    # Function to initialize LinkedList object
    def __init__(self) -> None:
        self.head = None # Initialize linked list with None/null as empty list
        self.tail = None

    # Function to add element at the start of linkedlist
    def add(self, data):
        # Create new Node, which will have data and next pointer as null/None          
        temp = Node(data)

        # if DoublyLinkedList itself is null/empty
        if (self.head == None):
            self.head = self.tail = temp
            return
        
        # Set next of newly created node's next pointer to tail, as we are adding at starting of linkedlist
        self.tail.next = temp
        # As new node next points to head, we have to create reverse link to temp as well
        temp.prev = self.tail
        # Now we have to reset our head to point to the first element of linkedlist again
        self.tail, self.tail.next = temp, None
        
    def insert(self, position, data):
        node = Node(data)
        if (position == 0):
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif (position == 1):
            temp = self.head.next
            temp.prev = node
            node.next = temp
            self.head.next = node
            node.prev = self.head
        else:
            temp = self.head
            for i in range(0, position):
                temp = temp.next
            
            if (temp == None):
                self.add(data)
            else:
                prev = temp.prev
                temp.prev = node
                node.next = temp
                node.prev = prev
                prev.next = node
            

    
    def print(self):
        temp = self.head
        while (temp):
            print(temp.data, end = ' ')
            temp = temp.next
        print('\n')


    
    def delete(self, data):
        # reference head in temporary variable
        temp = self.head

        # best case, if head is the element that we want to delete
        if (temp):
            if (temp.data == data):
                self.head = temp.next
                return
        
        # condition for other element apart from head        
        while (temp):
            if (temp.data == data):
                break
            else:
                temp = temp.next
            
        # check if no data found after full iteration then return,
        if (temp == None):
            return
        
        # if data is matched, then we have to dereference matched node and remove link, and move it to
        # next link immediate to temp next
        prev = temp.prev
        prev.next = temp.next        


# Testing portion
if __name__=='__main__':
 
    llist = DoublyLinkedList()
 
    llist.add(1)
    llist.add(2)
    llist.add(3)
    llist.add(4)
    llist.add(5)    
    llist.print()
    llist.delete(3)        
    llist.print()
    llist.insert(0, 6)
    llist.print()
    llist.insert(2, 8)
    llist.print()

    
