from typing import Any, TypeVar

class DNode:
    def __init__(self, data):
        self.data: Any = data 
        self._prev: self = None
        self._next: self = None 


