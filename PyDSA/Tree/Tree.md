# Tree Data Structure and Algorithm Tutorials

### What is a Tree data structure ?

A **tree data structure** is a hierarcical structure that is used to represent and organised data is a way taht is easy to navigate and search. It is a collectino of nodes that are connected by adges and has a hierarchical relationship between the nodes. 

The topmost ndoe of that tree is called the root, and the nodes below it are called the child nodes. Each nodes can have multiple child nodes, and these child nodes cal also have their own child nodes, forming a recursive structure.

### Recusive Definition

A tree consists of a root, and zero or more subtrees T1, T2, ..., Tk such there is an edge from the root of the tree to the root of each subtree.


### Tree are non linear data structure

The data in a tree are arranged on  multiple levels (hierarhical structrue).

### Structure

![image not found](TreeDataStructure.png "Binary Tree")

### Basic Terminology

- **Parent Node:** The node which is a predecessor of a node is called the parent node of that node.
- **Child Node:** The ndoe which is the immediate successor of a node is calld the child node of the node.
- **Root Node:** The topmost node of a tree or  the node which does not have any parent node is called the root node. A non-empty Tree must contain exactly one root node and exactly one path from the root to all other nodes of the tree.
- **Leaf Node or External Node:** The nodes which do not have any child nodes are called leaf nodes.
- **Ancestor of a Node:** Any predecessor nodes on the path of the root to that are called Ancestors of that nodes.
- **Descendant:** Any successor node on the path from tht leaf node to that node.
- **Sibling:** Children of the same parent node are called siblings.
- **Level of a node:** The cound of edges on the path from the root node to that node. The root node has level 0.
- **Internal node:** A node which at least one child is called Internal Node.
- **Neighbour of a Node:** Parent or child nodes of that node are called neighbors of that node.
- **Subtree:** Any node of that tree along with it decendant.

### Properties of a Tree;

- **Number of edges:** An edge can be defined as the connection between two nodes. If a tree has N nodes then it will have (N-1) edges. There is only one path from each node to any other node of the tree.
- **Depth of a node:** The depth of a node is defined as the lenght of the path from the root to that node. Each edge adds 1 unit of length to the path. So, it can also be be defined as the number of edges in the path from the root of the tree to that node.
- **Height of a node:** The height of a node can be defined as the length of the longest path from the node to the leaf node of that tree.
- **Height of the Tree:** The height of a tree is the length of the longest path from the root of the tree to a leaf node of the tree.
- **Degree of a Node:** The total count of subtrees attached to that node is called the degree of the node. The degree of a leaf node must be 0. The degree of a tree is the maximum degree of a node amoung all the nodes in the tree.

#### Some more properites are:

- Traversing in a tree is done by depth frist search and breadth first search algorithm.
- It has no loop and no circuit
- It has not self-loop
- Its hierarchical model.

### Basic operation of Tree:

- Create - create a tree in data structure
- Insert - Inserts data in tree.
- Search - Searches speicific data in a tree to check it is present or not.
- Preorder Traversal - perform Traveling a tree is a pre-order manner in data structure.
- In order Traversal - perform Traveling a tree in an in-order manner.
- Post order Traversal - perform Traveling a tree in a post-order manner.


## Types of Tree data structures

The different types of tree data structures are as follows:

### General tree 

A general tree data structure has no restriction on the number of nodes. It means that a parent node can have any number of child nodes.

### Binary tree 

A node of a binary tree can have