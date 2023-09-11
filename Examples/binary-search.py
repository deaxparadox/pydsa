import random
import typing


def binary_search(target: typing.Any, seq: typing.Sequence) -> None:
    if len(seq) == 0:
        raise RuntimeError("empty list")

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

    return

if __name__ == "__main__":
    array = [x for x in range(1, 11)]
    print(array)

    for i in range(3):
        target = random.randint(1, 10)
        bs = binary_search(target, array)
        print(f"target: {target}\nbinary search: {bs}\n")
