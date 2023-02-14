import queue


# The storage class for creating binary tree nodes.
class _BinTreeNode:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

def perorderTrav(subtree):
    if subtree is not None:
        print(subtree.data)
        perorderTrav(subtree.left)
        perorderTrav(subtree.right)

def inorderTrav(subtree):
    if subtree is not None:
        inorderTrav(subtree.left)
        print(subtree.data)
        inorderTrav(subtree.right)


def postorderTrav(subtree):
    if subtree is not None:
        postorderTrav(subtree.left)
        postorderTrav(subtree.right)
        print(subtree.data)


def breadthFirstTrav(bintree):
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