import typing
import random


class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

class Traversal(object):
    def preorder(self, node: Node):
        if node:
            print(f"{node.data}", end=" < ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node: Node):
        if node:
            self.inorder(node.left)
            print(f"{node.data}", end=" < ")
            self.inorder(node.right)

    def postorder(self, node: Node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(f"{node.data}", end=" < ")


class binary_tree(object):
    def __init__(self):
        self.head = None

    def insert(self, data) -> None:
        new_node: Node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            self._insert(self.head, new_node)

    def _insert(self, node: Node, new_node: Node) -> None:
        if new_node.data < node.data:
            if node.left is None:
                node.left = new_node
            else:
                self._insert(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self._insert(node.right, new_node)

def main():
    b = binary_tree()

    for i in range(10):
        value = random.randint(1, 100)
        b.insert(value)
        print(f"{value}", end=" ")
    print()

    t = Traversal()
    t.preorder(b.head)
    print()
    t.inorder(b.head)
    print()
    t.postorder(b.head)
    print()

if __name__ == "__main__":
    main()