# Binary Trees

A binary tree is a tree data structure in which each node has at the most two children, which are referred to as the left child and the right child.

- Binary tree is a collection of `nodes`. 
- Each `nodes` has three attributes:
    1. value
    2. left_child
    3. right-child


```python
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
```