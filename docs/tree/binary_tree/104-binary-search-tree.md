# Binary Search Tree

A Binary Search Tree is sometimes called ordered or sorted binary trees, and it keeps it values in sorted order, so that lookup and other operations can use the principle of binary search.

**An important property of a `Binary Serach Tree` is that the value of a `Binary Search Tree` node is larger that then the value of the offspring  of its `left child`, but smaller than the value of the offspring of its `right child`.**

![image not found](BST.md)

Here is a breakdown of the above illustration:

- **A** is inverted, The `subtree` 7-5-8-6 needs to be on the right side, and the `subtree` 2-1-3 needs to be on the left.
- **B** is the only correct option. It satisfies the `Binary Search Tree` property.
- **C** has one problem: the `node` with the value 4. It needs to be on the left side of the `root` because it is smaller than 5.

## Coding Binary Search Tree!

What will we see here?

- We will insert new nodes,
- search for a value, 
- delete nodes
- and the balance of the `tree`.