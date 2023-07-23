import argparse
import typing

class even(object):
    __match_args__ = ("start", "stop")

    def __init__(self, start: int = 0, stop: int = 0) -> None:
        self.__start = start
        self.__stop = stop
        if self.__stop == 0:
            self.__stop = self.__start
            self.__start = 0
        
        self.__even: int 

    def __calculate(self):
        p: bool = False
        # print("start:", self.__start)
        for n in range(self.__start, self.__stop):
            if n % 2 != 0:
                self.__start += 1
                pass
            else:
                self.__even = n
                self.__start += 1
                return
    

        
  
    def __iter__(self):
        return self
    
    def __next__(self, *args, **kwargs):
        self.__calculate()
        if self.__start == self.__stop:
            raise StopIteration
        return self.__even
