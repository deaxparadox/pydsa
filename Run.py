import argparse
import typing
import enum 


from PyDSA import Stack

class Func:
    stack: enum.auto = enum.auto()
    queue: enum.auto = enum.auto()


def argument():
    args = argparse.ArgumentParser()
    args.add_argument("FUNC")
    return args.parse_args()


def stack() -> None:
    with Stack() as q:
        with Stack() as s:
            for i in range(1, 10):
                s.append(i)
                q.append(i)
            s.print()
            print(s)
            print("Length: ", len(s))

            print("Removing: ", s.remove(5))
            print(s)
            print("Removing: ", s.remove(15))
            print(s)
            print("Length: ", len(s))

            print("Deleted: ", s.pop())
            print("Length: ", len(s))
            s.print()
            print(s)

            print('for', end=" -> ")
            for i in s:
                print(i, end=", ")
            print()
            s[1] = "Nitish"
            print("First: ", s[0])
            print("Second:", s[1])

            while True:
                try:
                    d = s.pop()
                    print(d)
                except:
                    print("Pop from empty stack.")
                    break


def main() -> None:
    arg = argument()
    if arg.FUNC == "stack":
        stack()

if __name__ == "__main__":
    main()