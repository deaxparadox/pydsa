from rich.panel import Panel
import rich 
from rich.emoji import Emoji
from rich.box import Box
from typing import Any
from ..EmptyClass import BaseStack

class Node(object):
    def __init__(self, data: Any) -> None:
        self.data: Any = data 
        self._nex: self  = None
    
    

class Stack(BaseStack):
    def __init__(self):
        self.__head: Node | None = None
        self.__tail: None | None = None
        self.__len = 0
        
    def __len__(self):
        return self.__len

    def __eq__(self, other: Node) -> None:
        return self.__len == len(other)

    def __str__(self):
        return f"[{self.print(ret=True)}]"

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, index: int):
        temp: Node = self.__tail
        for i in range(index):
            if temp is None:
                raise IndexError("Index exceed length")
            temp = temp._nex
        return temp.data

    def __setitem__(self, index: int, data: Any) -> None:
        temp: Node = self.__tail
        for i in range(index):
            if temp is None:
                raise IndexError("Index exceed length")
            temp = temp._nex
        temp.data = data

    @property
    def data(self):
        return self.__tail.data

    def append(self, data):
        # new node 
        new_node: Node = Node(data)
        
        # if head is None
        if self.__head is None:
            self.__tail = self.__head = new_node
            self.__len += 1
        else:
            new_node._nex = self.__tail 
            self.__tail = new_node
            self.__len += 1
            

    def pop(self) -> Any:
        if self.__tail is None:
            raise IndexError("Stack is empty.")
        temp, data = self.__tail, self.__tail.data
        self.__tail = self.__tail._nex
        self.__len -= 1
        del temp
        return data

    def remove(self, data) -> Any | None:
        # ptr: Node | None = self.__tail
        # nex: Node | None = None
        # data: Any
        # while ptr:
        #     if ptr.data == data:
        #         print("found match")
        #         data = ptr.data
        #         nex._nex = ptr._nex
        #     nex = ptr
        #     ptr = ptr._nex

        # del nex
        # del ptr
        # return data

        ptr: Node = self.__tail
        nex: Node = ptr
        while ptr:
            if ptr.data == data:
                # print("found match")
                nex._nex = ptr._nex
                self.__len -= 1
                break
            nex = ptr
            ptr = ptr._nex
        if ptr is None:
            raise ValueError("Value not found.")

        del nex
        del ptr
        
    
    def print(self, ret=False):
        temp = self.__tail
        lst = []
        while temp:
            # print(temp.data, end=", ")
            lst.append(str(temp.data))
            temp = temp._nex
        lst = ",".join(lst)
        if ret:
            return lst
        else:
            print(lst)
        # rich.print(
        #     Panel(
        #         ",".join([str(x) for x in self]), 
        #         border_style="cyan", 
        #         expand=False
        #     )
        # )
    
    def is_empty(self):
        return self.__len == 0

    def __iter__(self):
        self.__iter: Node = self.__tail
        return self
    def __next__(self):
        if self.__iter is None:
            raise StopIteration
        data = self.__iter.data
        self.__iter = self.__iter._nex
        return data

    def __enter__(self):
        return self 
    def __exit__(self, *args, **kwargs):
        return 

