import unittest

# Node class 
class Node:
    def __init__(self, item):
        self.item = item 
        self.leftChild = None 
        self.rightChild = None 


# Checking full binary tree 
def isFullTree(root: Node):
    
    # Tree emtpy case 
    if root is None:
        return True 
    
    # Checking whether child is present 
    if root.leftChild is None and root.rightChild is None:
        return True 

    if root.leftChild is not None and root.rightChild is not None:
        return isFullTree(root.leftChild) and isFullTree(root.rightChild)

    return False

