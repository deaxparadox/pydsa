from typing import Any, TypeVar

from .node import DNode


List = TypeVar("List", bound="List")

class List:
    def __init__(self):
        self._head: DNode | None = None 
        self._tail: DNode | None = None
        self.__len = 0

    def __len__(self) -> int:
        return self.__len

    def __string_form(self) -> str:
        ret = "["
        for i in self:
            ret += f"{i},"
        ret += "]"
        return ret

    def __str__(self) -> str:
        return self.__string_form()
    
    def __repr__(self) -> str:
        return self.__string_form()

    def __eq__(self, other: DNode) -> bool():
        return self.__len == len(other)
    

    # iterator

    def __iter__(self) -> List:
        self._iter: DNode = self._head
        return self 
    def __next__(self):
        if self._iter is None:
            raise StopIteration("List if empty!")
        data = self._iter.data
        self._iter = self._iter._next
        return data

    # context manager

    def __enter__(self) -> List:
        return self 
    def __exit__(self):
        return 

    
    def is_empty(self) -> bool:
        return self.__len == 0

    def append(self, data: Any) -> None:
        new_node: DNode = DNode(data)

        if self._head is None and self._tail is None:
            self._head = self._tail = new_node
            self.__len += 1
        else:
            new_node._prev = self._tail
            self._tail._next = new_node
            self._tail = new_node
            self.__len += 1

    def pop(self):
        rem, data = self._tail, self._tail.data
        self._tail = self._tail._prev
        self._tail._next = None
        del rem 
        return data 

    def insert(self, data):
        new_node: DNode = DNode(data)

        if self._head is None and self._tail is None:
            self._head = self._tail = new_node
            self.__len += 1
        else:
            new_node._next = self._head
            self._head._prev = new_node
            self._head = new_node
            self.__len += 1

    def remove(self, data: Any | None = None):
        rem, data = self._head, self._head.data
        self._head = self._head._next
        self._head._prev = None
        del rem
        return data

    def print(self):
        for i in self:
            print(i, end=" ")
        print()        




    
