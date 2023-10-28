from typing import Any, Callable


class FibonacciDP(object):
    __dpdict: dict = {}

    def __init__(self, *args, **kwargs) -> None:
        self.__args = args
        self.__kwargs = kwargs
        self.__num: int | None = None
    
    def wrapper(self):
        if self.__num is None:
            raise RuntimeError("Number of supplied!")
        value = self.algorithm(self.__num)
        self.__dpdict[self.__num] = value
        return value
    
    def of(self, num: int):
        self.__num = num
        return self

    def algorithm(self, num: int):
        if num in self.__dpdict: 
            return self.__dpdict[num]
        match num:
            case 0:
                return 0
            case 1:
                return 1
        return self.algorithm(num - 1) + self.algorithm(num-  2)


    def run(self) -> Any:
        return self.wrapper()
    
if __name__ == "__main__":
    c = FibonacciDP()
    for i in range(1, 40):
        print(c.of(i).run())