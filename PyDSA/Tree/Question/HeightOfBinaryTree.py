import typing

class Node:
    def __init__(self, x) -> None:
        self.data = x
        self.left = self.right = None

def _insert(root: Node, new_node: Node) -> None:
    if new_node.data < root:
        if root.left is None:
            root.left = new_node
        else:
            _insert(root.left, new_node)
    else:
        if root.right is None:
            root.right = new_node
        else:
            _insert(root.right, new_node)

def insert(root: Node | None, x: int) -> None:
    new_node = Node(x)
    if root is None:
        root = new_node
    else:
        _insert(root, new_node)


def findDepth(root: Node, x: typing.Any) -> int:
    if (root == None): return -1

    dist=-1

    if (root.data == x): return dist+1 

    dist = findDepth(root.left, x)
    if dist >= 0: return dist+1 

    dist = findDepth(root.right, x)
    if dist >= 0: return dist+1

    return dist


def main() -> None:
    root = Node(1)
    insert(root, 12)
    insert(root, 143)
    insert(25)

    d = findDepth(root, 25)
    print(d)

if __name__ == "__main__":
    main()