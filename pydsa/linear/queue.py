from rich.panel import Panel
import rich 
from rich.emoji import Emoji
from rich.box import Box
from typing import Any, Sequence

class Node:
    def __init__(self, data):
        self.data = data 
        self._nex = None


class Queue:
    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__len: int = 0

    def __len__(self) -> int:
        return self.__len

    def __str__(self) -> str:
        return f"[ {self.print(ret=True)} ]"

    def __eq__(self, other: Node) -> bool:
        return self.__len == len(other)

    def __iter__(self):
        self.__iter: Node = self.__head
        return self
    def __next__(self):
        if self.__iter is None:
            raise StopIteration("Queue is empty!")
        data = self.__iter.data
        self.__iter = self.__iter._nex
        return data

    def __enter__(self):
        return self 
    def __exit__(self, *args, **kwargs):
        return 

    def is_empty(self) -> bool:
        return self.__len == 0 


    def insert_first(self, data) -> None:
        new_node: Node(data) = Node(data)

        if self.__head is None:
            self.__head = self.__tail = new_node
            self.__len += 1
        else:
            self.__tail._nex = new_node
            self.__tail = new_node
            self.__len += 1
            

    def remove_first(self) -> None:
        if self.__head is None:
            raise IndexError("Queue is empty")
        temp, data = self.__head, self.__head.data
        self.__head = self.__head._nex 
        self.__len -= 1
        del temp
        return data
    
    def print(self, ret: bool = False):
        # temp = self.__head 
        # lst = []
        # while temp:
        #     lst.append(str(temp.data))
        #     temp = temp._nex
        # lst = " < ".join(lst)
        # if ret:
        #     return lst
        # else:
        #     print(lst)
        #     return 
        
        
        rich.print(
            Panel(
                ",".join([str(x) for x in self]), 
                border_style="cyan", 
                expand=False
            )
        )

        
        
    
def main():
    q = Queue()
    for i in range(1,10):
        q.insert_first(i)
    q.print()
    q.remove_first()
    q.print()
    print(q)
    while True:
        try:
            q.remove_first()
        except:
            print("Queue empty!")
            break

if __name__ == "__main__":
    main()