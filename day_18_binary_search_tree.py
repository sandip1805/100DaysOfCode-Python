class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def __insertHelper(self, root, data):
        node = Node(data)
        if (root == None):
            root = node
        elif(data <= root.data):
            root.left = self.__insertHelper(root.left, data)
        else:
            root.right = self.__insertHelper(root.right, data)
        return root

    def insert(self, data):
        self.root = self.__insertHelper(self.root, data)
    
    def __searchHelper(self, root, data):
        if (root == None or root.data == data):
            return root
        if (data < root.data):
            return self.__searchHelper(root.left, data)
        else:
            return self.__searchHelper(root.right, data)

    def search(self, data):
        return self.__searchHelper(self.root, data)

    def __findMinHelper(self, root):
        if (root == None):
            return None
        elif(root.left == None):
            return root.data
        else:
            return self.__findMinHelper(root.left)

    def findMin(self):
        return self.__findMinHelper(self.root)

    def __findHeight(self, root):
        if (root == None):
            return -1
        leftWeight = self.__findHeight(root.left)
        rightWeight = self.__findHeight(root.right)
        return max(leftWeight, rightWeight) + 1

    def findHeight(self):
        return self.__findHeight(self.root)
    
    def __inorder(self, root):
        if root:
            self.__inorder(root.left)
            print(root.data, end=' ')
            self.__inorder(root.right)
        
    def printInOrder(self):
        self.__inorder(self.root)
        print('\n')


if __name__ == "__main__":
    print("Binary Search Tree!!!")
    bst = BinarySearchTree()    
    bst.insert(10)
    bst.insert(7)
    bst.insert(14)    
    bst.insert(8)
    bst.insert(6)    
    bst.insert(13)
    bst.insert(19)
    bst.insert(3)
    bst.insert(15)
    bst.insert(4)
    bst.insert(21)
    bst.printInOrder()
    print(f'Search data: {bst.search(13).data}')
    print(f'Find minimum data: {bst.findMin()}')
    print(f'Find height of BST: {bst.findHeight()}')
        
