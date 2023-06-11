from typing import Any, Self

limit = 10

class BranchInt(object):
    def __init__(self, data: int, /) -> None:
        if self.__init__.__annotations__.get("data") == type(data):
            pass 
        else:
            raise TypeError("data must be integer")
        self.data: int = data
        self.branches: list[int] = []

class BranchString(object):
    def __init__(self, data: str, /) -> None:
        if self.__init__.__annotations__.get("data") == type(data):
            pass 
        else:
            raise TypeError("data: must be integer")
        self.data: str = data
        self.branches: list[str] = []

class Branch(object):
    def __init__(self, data: Any, /, *, limit: int = limit) -> None:
        self.__data: Any = data
        self.__branches: list[Any] = []
        self.__limit: int = limit
      
    # get object with indexing  
    def __getitem__(self, index: int, /) -> Any:
        if self.__getitem__.__annotations__.get("index") == type(index):
            pass 
        else:
            raise TypeError("index: must be integer")
        return self.__branches[index]
    # set object using inde indexing
    def __setitem__(self, index: int, data: Any, /) -> Any:
        if self.__setitem__.__annotations__.get("index") == type(index):
            pass 
        else:
            raise TypeError("index: must be integer")
        self.__branches[index] = data
    

    # check if branch is full
    def is_full(self, /) -> bool:
        return len(self.__branches) == self.__limit
    
        
    # get branch data
    @property
    def branch(self, /) -> None:
        return self.__data
    
    # get all branches
    @property
    def branches(self, /) -> None:
        return self.__branches
    
    # add branch
    # return False, if branch is full
    # return True, if new branch is added
    def add_branch(self, new_branch: Any, /) -> bool:
        if self.is_full():
            return False
        else:
            self.__branches.append(new_branch)
            return True
        
    def __str__(self):
        return r"{0}, {1}".format(self.__data, self.branches)
    
    def __repr__(self):
        return r"{0}, {1}".format(self.__data, self.branches)
    
    
    # iterator
    def __iter__(self):
        for i in self.branches:
            yield i
            
    # context manager
    def __enter__(self) -> Self:
        return self
    def __exit__(self, *args, **kwargs) -> None:
        return 