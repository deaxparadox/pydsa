# Tree Data Structure

A tree structure consists of nodes and edges that organize data in a hierarchial fashion.

The relatioships between data elements in a tree are similar to those of a family tree: "child", "parent", "ancestor", etc.\

The data elements are stored in **nodes** and apris of nodes are connect by **edges**.

The edges represent the relationship between the nodes that are linked with arrows or directed edges to form a **hierarchical structure** resembling an upside-down tree complete with branches, leaves, and even a root.

Example is the UNIX file system.


#### Root 

The topmost node of the tree is konwn as the **root node**. It provides the signle access point into the structure.

Every non-empty tree must contain a root node.


#### Path 

The other nodes in the tree are accessed by following the edges starting with the root and progressing in the direction of the arrow untill the destination node is reached.

The nodes encountered when following the edges from a starting node to a destination form a **path**.


#### Parent

Evert node, except the root, has a **parent node**, which is identified by the incomming edge.


#### Children

Every node can have noe or more **child** node resulting in a parent-child relationship.

All nodes that have the same parent are known as siblings.

#### Nodes 

Nodes that have at least noe child are known as **interior nodes** while nodes that have no children are known as **leaf nodes**.


#### Subtree 

Every node can be the root of its own **subtree**, which consists of a subset of nodes and edges of the larger tree.


#### Relative 

All of the nodes in a subtree are descendants of the subtrees's root. 

The ancestors of a node include the parent of the node, its grandparent, its great-grandparent, and so on all the way up to the root.

The root node is the ancestor of every node in the tree and every node in the tree is a descendant of the root node.


## Binary Tree

A *binary tree* is a tree in which each node can have at most two children. One child is identified as the *left child* and the other as the *right child*


### Properties 

#### Tree Size

The nodes in a binary tree are organized into *levels* with the root node at level 0, its children at level 1, the children of level one nodes are at level 2, and so on.

The *depth* of a node is its distance from the root, with distance being the number of levels that separate the two.

The *height* of a binary tree is the number of levels in the tree.

The *width* of  binary tree is the number of nodes on the level containing the most nodes.

The *size* of a binary tree is simpy the number of nodes in the tree.

A binary tree of size n can have a maximun height of n, which results when there is one node per level.

Tree with level *i* will have a capacity *2^i* nodes.

The minimum height of a binary tree of size n is [log n base2] + 1


### Tree Structure 

#### Full binary Tree 

It is a binary tree in which each interior node contains two children

#### Perfect binary Tree 

It is a full binary tree in which all leaf nodes are at the save level. The perfect tree has all possible node slots filled from top to bottom with no gaps.



A binary tree of height *h* is a *complete binary tree* if it is perfect binary tree down to height *h* - 1 and the nodes on the lowest level fill the available slots from left to right leaving no gaps.


### Tree Traversal

##### Preorder Traversal 

In pre-order traversal left subtree if always visited before the tright subtree.

##### Inorder Traversal 

In inorder traversal we first visit the left subtree, then visit the node followed by the traversal of the right subtree.

##### Postorder Traversal 

In postorder traversal subtrees are visited first then the node node is visited.


#### Breadth-First Traversal

The preorder, inorder, postorder traversals are all example of a **depth-first traversal**. That is, the nodes are traversed deeper in the tree before returning to higher-level nodes.

In **breadth-first traversal**, the nodes are visited by level, from left to right.