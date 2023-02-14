import typing

class Base(object):
    def __init__(self) -> None:
        pass 
    def __eq__(self) -> bool():
        pass
    def __len__(self) -> int:
        pass 
    def __str__(self) -> str:
        pass 
    def __repr__(self) -> str:
        pass 
    def __getitem__(self) -> None:
        pass 
    def __setitem__(self) -> None:
        pass 
    
    # Iteration
    def __iter__(self) -> object:
        self
    def __next__(self) -> typing.Any:
        pass 
    
    # context manager
    def __enter__(self) -> object:
        return self
    def __exit__(self, *args, **kwargs) -> None:
        return 


class BaseStack(Base):
    def append(self) -> None:
        pass 
    def pop(self) -> typing.Any:
        pass 
    def is_empty(self) -> bool:
        pass 
    def remove(self) -> None:
        pass 
    def print(self) -> str:
        pass 

class BaseQueue(Base):
    def insert(self) -> None:
        pass 
    def remove(self) -> typing.Any:
        pass 
    def is_empty(self) -> bool:
        pass 
    def remove(self) -> None:
        pass 
    def print(self) -> str:
        pass 

class BaseDouble(Base):
    def append(self) -> None:
        pass 
    def pop(self) -> typing.Any:
        pass 
    def insert(self) -> None:
        pass 
    def remove(self) -> typing.Any:
        pass 
    def is_empty(self) -> bool:
        pass 
    def remove(self) -> None:
        pass 
    def print(self) -> str:
        pass 