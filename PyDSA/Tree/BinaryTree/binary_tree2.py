import os
from dataclasses import dataclass
import typing

file = "/home/creator/Documents/Paradox/Github/DSA/Python/files/words_list.txt"


@dataclass(init=True, repr=True)
class Word:
    ...
    
class f:
    @staticmethod
    def read_file(file: str) -> typing.List[str]:
        words: typing.List[str] = []
        with open(file, "r") as f:
            for line in f.readlines():
                words.append(line.strip())
        return words


SelfNode = typing.TypeVar("SelfNode", bound="Node")
class Node:
    def __init__(self, data):
        self.data: str = data
        self.nodes: list[self] = []

    def __str__(self: SelfNode) -> str:
        return self.data

    def __eq__(self: SelfNode, other: SelfNode) -> bool:
        return self.data == other.data


# words = f.read_file(file)
# for word in words:
#     if word.__len__() > 1:
#         print(word, end="\t")

a = Node('a')
b = Node('b')
print(f"a: {a}, b: {b}")
print(f"a == b : {a==b}")
print(f"a is b : {a is b}")
print(isinstance(a, Node))