from typing import Any, TypeVar
import warnings

from pydsa import Stack, Queue



class GraphAlgorithm(object):
    def DepthFirstSearchLinear(self, source: Any | None = None, stack: Stack = None):
        pass    
    def DepthFirstSearchRecursion(self, source: Any | None = None, stack: Stack = None):
        pass    
    def BreadthFirstSearch(self, source: Any | None = None, queue: Queue = None):
        pass 


GraphSelf =TypeVar("Graph")
class Graph(GraphAlgorithm):
    def __init__(
        self, 
        graph: dict | None = None,
    ) -> None:
        self._undirected = False
        self._stack = Stack()
        self._queue = Queue()
        self._graph = graph
        self._temp: bool = False
    
    def DirectedLoadTemporary(self) -> GraphSelf:
        """
        Load the defalt graph,

        graph = {
            "a": ['b', 'c'],
            "b": ['d'],
            "c": ['e'],
            "d": ['f'],
            "e": [],
            "f": [],
        }

        Set default source: 'a'

        Add default source to stack

        """
        if self._temp:
            raise 

        warnings.warn("Loading default data")
        self._graph = {
            "a": ['b', 'c'],
            "b": ['d'],
            "c": ['e'],
            "d": ['f'],
            "e": [],
            "f": [],
        }
        self._source = 'a'
        self._stack.append(self._source)
        self._queue.insert_first(self._source)
        self._temp = True
        return self

    def DepthFirstSearchLinear(self, source: Any | None = None) -> None:
        if self._temp == False:
            self._stack.append(source)
        
        while len(self._stack) > 0: 
            current = self._stack.pop()
            print(current, end=",")
            for neighbor in self._graph[current]:
                self._stack.append(neighbor)
        print()

    def BreadthFirstSearch(self, source: Any | None = None) -> None:
        if self._temp == False:
            self._queue.insert_first(source)
        
        while len(self._queue) > 0: 
            current = self._queue.remove_first()
            print(current, end=",")
            for neighbor in self._graph[current]:
                self._queue.insert_first(neighbor)
        print()