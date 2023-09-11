import typing

def linear_serach(target: typing.Any, seq: typing.Sequence) -> int | None:
    """
    LINEAR SEARSH ALGORITHM

    It take array and target to be targated, or simple element to be found in 
    array, and return index if target exist in array else None
    """

    if len(seq) == 0:
        raise RuntimeError("Empty list")
    
    i, j = 0, len(seq)

    while i < j:
        if seq[i] == target:
            return i
        i+=1

    return
        