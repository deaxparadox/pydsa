# Binary Trees

A binary tree is a tree data structure in which each node has at the most two children, which are referred to as the `left_child` and the `right_child`.

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

When we instantiate an object, we pass the `value` as a parameter.

```python
tree = BinaryTree('a')
print(tree.value) # a
print(tree.left_child) # None
print(tree.right_child) # None
```

- We will implement a method to insert a new `node` to the `right` and to the `left`:

    - If the current `node` doesn't have `left_child`, we create a new `node` and set it to the current node's `left_child`.
    - if it does have the `left_child`, we create a new node and put it in the current `left_child`'s place. Allocate this `left_child` node to the new node's `left_child`.
    - And we do the same thing to insert a `right_child` node.

```python
def insert_left(self, value):
    if self.left_child == None:
        self.left_child = BinaryTree(value)
    else:
        new_node = BinaryTree(value)
        new_node.left_child = self.left_child
        self.left_child = new_node
```

To summarize the illustration of this tree:

1. `a` `node` will the `root` of our `binary_tree`
2. `a` `left_child` is `b` `node`
3. `a` `right_child` is `c` `node`
4. `b` `right_child` is `d` node (`b` node doesn’t have a left child)
5. `c` `left_child` is `e` node.
6. `c` `right_child` is `f` node.
7. both `e` and `f` nodes do not have children

So here is the code for the tree:

```python
a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_right('d')

c_node = a_node.right_child
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child

print(a_node.value) # a
print(b_node.value) # b
print(c_node.value) # c
print(d_node.value) # d
print(e_node.value) # e
print(f_node.value) # f
```

[Tree Traversal >>>](101-traversal.md)