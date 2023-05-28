import random


from queue import Queue


class Node:
    def __init__(self, data):
        self.__info = data 
        self.__left: Node = None
        self.__right: Node = None 

    @property
    def data(self) -> int:
        return self.__info
    @data.setter
    def data(self, value: int):
        self.__info = value

    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, value):
        self.__left = value
        
    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, value):
        self.__right = value
        

class BinaryTree(object):
    def __init__(self) -> None:
        self.__root: Node | None  = None

    @property
    def root(self) -> Node | None:
        return self.__root

    @root.setter
    def root(self, data: Node | None) -> None:
        self.__root = data

    def insert(self, data: int):
        new_node: Node = Node(data)

        if not self.root:
            self.root = new_node
        else:
            self.__insert(self.root, new_node)

    def __insert(self, root: Node, new_node: Node, /):
        if new_node.data < root.data:
            if not root.left:
                root.left = new_node
            else:
                self.__insert(root.left, new_node)
        else:
            if not root.right:
                root.right = new_node
            else:
                self.__insert(root.right, new_node)


class Operation(object):
    def inorder(self, root: Node):
        """
        Inorder operation on binary tree.

        In this operation we access left subtree, then data, then right subtree.
        
        root -- accepts argument as `Node` type.
        """
        if root:
            self.inorder(root.left)
            print(root.data, end=" -> ")
            self.inorder(root.right)
        return
    
    def preorder(self, root: Node, /):
        """
        Preorder operation on binary tree.

        Structure of  operation:
            - node.data
            - node.left
            - node.right

        Argument:
        root -- `Node` type
        """
        if root:
            print(root.data, end=" -> ")
            self.preorder(root.left)
            self.preorder(root.right)
        return
    
    def preorder_no_recur(self, root: Node) -> None:
        if not root:
            return 
        
        stack = []

        while root or stack:
            if root:
                print(root.data, end=" -> ")
                stack.append(root)
                root: Node = root.left
            else:
                root: Node = stack.pop()
                root = root.right

    def postorder(self, root: Node, /):
        if root:  
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" -> ")
        return

    def postorder_no_recur(self, root: Node, /):
        if not root:
            return 
        
        queue: Queue = Queue()

        while root or queue.empty():
            if root:
                print(root.data, end=" -> ")
                queue.put(root)
                root: Node = root.left
            else:
                root: Node = queue.get()
                root = root.right
    

if __name__ == "__main__":
    a = [random.randint(1, 100) for _ in range(10)]

    b = BinaryTree()
    
    for i in a:
        b.insert(i)

    o = Operation()
    o.inorder(b.root) 
    print()
    
    # o.preorder(b.root)
    # print()
    # o.preorder_no_recur(b.root)
    # print()

    o.postorder(b.root)
    print()
    o.postorder_no_recur(b.root)
    print()