import typing

def binary_search(seq: typing.Sequence|None = None, target: typing.Any|None = None,  *args):
    if len(seq) == 0 and len(args) == 0:
        raise RuntimeError("no iterable bound.")
    
    if not target:
        raise RuntimeError("target not found.")

    if len(seq) > 0:    
        start = 0
        stop = len(seq) - 1

        while start <= stop:
            mid = start + (stop-start) // 2  

            if seq[mid] > target:
                stop = mid - 1
            elif seq[mid] < target:
                start = mid + 1
            else:
                return mid

    return -1