from typing import Any, Sequence

class Node:
    def __init__(self, data):
        self.data = data 
        self._nex = None


class Queue:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.len: int = 0

    def __len__(self) -> int:
        return self.len

    def __str__(self) -> str:
        return f"[ {self.print(ret=True)} ]"

    def __eq__(self, other: Node) -> bool:
        return self.len == len(other)

    def is_empty(self) -> bool:
        return self.len == 0 


    def insert_first(self, data) -> None:
        new_node: Node(data) = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail._nex = new_node
            self.tail = new_node
            

    def remove_first(self) -> None:
        if self.head is None:
            raise IndexError("Queue is empty")
        temp, data = self.head, self.head.data
        self.head = self.head._nex 
        del temp
        return data
    
    def print(self, ret: bool = False):
        temp = self.head 
        lst = []
        while temp:
            lst.append(str(temp.data))
            temp = temp._nex
        lst = " < ".join(lst)
        if ret:
            return lst
        else:
            print(lst)
            return 

    
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