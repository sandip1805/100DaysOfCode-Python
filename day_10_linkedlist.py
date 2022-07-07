#Node class
from sniffio import current_async_library


class Node:
    # Function to initialize the node object
    def __init__(self, data) -> None:
        self.data = data # Assign data to instance variable
        self.next = None # initialize next with none/null

class LinkedList:
    # Function to initialize LinkedList object
    def __init__(self) -> None:
        self.head = None # Initialize linked list with None/null as empty list

    # Function to add element at the start of linkedlist
    def add(self, data):
        # Create new Node, which will have data and next pointer as null/None          
        temp = Node(data)
        # Set next of newly created node's next pointer to head, as we are adding at starting of linkedlist
        temp.next = self.head                    
        # Now we have to reset our head to point to the first element of linkedlist again
        self.head = temp
    
    def print(self):
        temp = self.head
        while (temp):
            print(temp.data, end = ' ')
            temp = temp.next

    def reverse(self):
        print('\nreversing elements\n')
        prev = None
        next = None
        current = self.head
        while (current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    
    def reverseRecursive(self):
        print('\n Recursive Reverse\n')
        # Call a recursiveReverse function with passing global head here.
        self.recursiveReverse(self.head)

    def recursiveReverse(self, curr):
        # Exit Condition for recursion, otherwise it will go into conitnuos loop,
        # if next is none, we are at the last node and we can assing head to that node
        if (curr.next == None):
            self.head = curr
        else:
            # Before starting recursion, always take previous node as a reference so that after recursive
            # call we can assing next node to previous one to reverse element
            prev = curr
            curr = curr.next
            self.recursiveReverse(curr)
            # one out of recursion, assign next as a prev and set prev.next as none otherwise it has a refrence of earlier state
            curr.next = prev
            prev.next = None


    
    def delete(self, data):
        # reference head in temporary variable
        temp = self.head

        # best case, if head is the element that we want to delete
        if (temp):
            if (temp.data == data):
                self.head = temp.next
                return
        
        # condition for other element apart from head
        prev = None
        while (temp):
            if (temp.data == data):
                break
            prev = temp
            temp = temp.next

        # check if no data found after full iteration then return,
        if (temp == None):
            return
        
        # if data is matched, then we have to dereference matched node and remove link, and move it to
        # next link immediate to temp next
        prev.next = temp.next


# Testing portion
if __name__=='__main__':
 
    llist = LinkedList()
 
    llist.add(1)
    llist.add(2)
    llist.add(3)
    llist.add(4)
    llist.add(5)
    
    llist.print()
    llist.delete(3)
    print('\n---------------------')
    llist.add(15)
    llist.print()
    llist.reverse()
    llist.print()

    print('\n---------------------')
    llist.reverseRecursive()
    llist.print()

    print('\n---------------------')
    llist.add(18)
    llist.print()
    llist.reverseRecursive()
    llist.print()

