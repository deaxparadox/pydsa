import enum
import typing 

class Traversal(enum.Enum):
    Preorder: enum.auto = enum.auto()
    Postorder: enum.auto = enum.auto()
    Inorder: enum.auto = enum.auto()


class Node(object):
    def __init__(self, data):
        self.value = data 
        self.left, self.right = None, None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert_node(self, root: Node, new_node: Node) -> None:
        if new_node.value < root.value:
            if root.left is None:
                root.left = new_node
            else:
                self.insert_node(root.left, new_node)
        else:
            if root.right is None:
                root.right = new_node
            else:
                self.insert_node(root.right, new_node)

    def insert(self, data: typing.Any) -> None:
        new_node: Node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self.insert_node(self.root, new_node)
            

    def print_tree(self, traversal_type):
        if traversal_type == Traversal.Preorder:
            return self.preorder_print(self.root, "")
        elif traversal_type == Traversal.Postorder:
            return self.postorder_print(self.root, "")
        elif traversal_type == Traversal.Inorder:
            return self.inorder_print(self.root, "")
        else:
            return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

if __name__ == '__main__':
    tree = BinaryTree()
    # tree.insert(15)
    # tree.insert(25)
    # tree.insert(10)
    # tree.insert(7)
    # tree.insert(22)
    # tree.insert(17)
    # tree.insert(13)
    # tree.insert(5)
    # tree.insert(9)
    # tree.insert(27)
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.insert(10)
    tree.insert(12)
    tree.insert(13)
    tree.insert(14)
    tree.insert(15)
    tree.insert(16)
    tree.insert(17)
    tree.insert(18)
    
    # tree.root.left = Node(2)
    # tree.root.right = Node(3)

    # tree.root.left.left = Node(4)
    # tree.root.left.right = Node(5)
    # tree.root.right.left = Node(6)
    # tree.root.right.right = Node(7)
    # tree.root.right.right.right = Node(8)

    print("Preorder: ", tree.print_tree(Traversal.Preorder))
    print("Inorder: ", tree.print_tree(Traversal.Inorder))
    print("Postorder: ", tree.print_tree(Traversal.Postorder))
    

