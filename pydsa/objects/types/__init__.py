from ..english import alphabet

class StringType(str):
    """
    Subclass the `str` type,

    1. added the length property for calculating length
    """
    @property
    def length(self):
        return len(self)
    
    def __calculate_weight(self) -> int:
        self_list = [x for x in self]
        return sum([getattr(alphabet, x).weight for x in self_list])

    @property
    def weight(self) -> int:
        return self.__calculate_weight()
    

class ListType(list):
    """
    Subclass the `list` type,

    1. added the length property for calculating length
    """

    @property
    def length(self):
        return len(self)