from typing import Any 

from .Node import DNode

class List:
    def __init__(self):
        self.head: DNode | None = None 
        self.tail: DNode | None = None
        self.len = 0

    def __len__(self) -> int:
        return self.len

    def __str__(self) -> str:
        return 

    def __eq__(self, other: DNode) -> bool():
        return self.len == len(other)

    def is_empty(self) -> bool:
        return self.len == 0

    def append(self, data: Any) -> None:
        new_node: DNode = DNode(data)

        if self.head is None and self.tail is None:
            self.head = self.tail = new_node
