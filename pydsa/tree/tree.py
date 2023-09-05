import queue


# The storage class for creating binary tree nodes.
class _BinTreeNode:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

def perorder(subtree):
    if subtree is not None:
        print(subtree.data)
        perorder(subtree.left)
        perorder(subtree.right)

def inorder(subtree):
    if subtree is not None:
        inorder(subtree.left)
        print(subtree.data)
        inorder(subtree.right)


def postorder(subtree):
    if subtree is not None:
        postorder(subtree.left)
        postorder(subtree.right)
        print(subtree.data)


def breadth_first_traversal(bintree):
    # Create a queue and add the root node to it.
    q = queue.Queue()
    q.put(bintree)

    # Visit each node in the tree.
    while not q.empty():
        node= q.get()
        print(node.data)

        # Add the two children to the queue.
        if node.left is not None:
            q.put(node.left)

        if node.right is not None:
            q.put(node.right)