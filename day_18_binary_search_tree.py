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
    bst.insert(15)

    bst.printInOrder()
        
