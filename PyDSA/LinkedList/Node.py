from typing import Any, TypeVar

class DNode:
    def __init__(self, data):
        self.data: Any = data 
        self.pre: self
        self.nex: self 


