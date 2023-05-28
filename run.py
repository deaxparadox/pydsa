import argparse
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import typing
import rich
from rich.panel import Panel
import enum 

class RPanel(object):
    @staticmethod 
    def RedBox(data: typing.Any | None = None):
        rich.print(Panel(f"[red]{data}[/red]", expand=False, border_style="red"))
    def CyanBox(data: typing.Any | None = None):
        rich.print(Panel(f"[cyan]{data}[/cyan]", expand=False, border_style="cyan"))
    def YellowBox(data: typing.Any | None = None):
        rich.print(Panel(f"[yellow]{data}[/yellow]", expand=False, border_style="yellow"))

from pydsa import Stack, Queue, Graph, List

class Func:
    stack: str = "stack"
    queue: str = "queue"
    graph: str = "graph"
    double: str = "double"


def argument():
    args = argparse.ArgumentParser()
    args.add_argument("FUNC")
    return args.parse_args()

def queue() -> None:
    with Queue() as q:
        for i in range(10):
            q.insert_first(i)
        q.print()
        for i in q:
            print(q.remove_first(), end=",")
        print()

def stack() -> None:
    with Stack() as q:
        with Stack() as s:
            for i in range(1, 10):
                s.append(i)
                q.append(i)
            s.print()
            print(s)
            print("Length: ", len(s))

            rich.print(Panel.fit(f"{s.data} {s}", style="red"))

            print("Removing: ", s.remove(5))
            print(s)
            rich.print(Panel.fit(f"{s.data} {s}", style="red"))
            # print("Removing: ", s.remove(15))
            # print(s)
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

                

def graph():
    g: Graph = Graph()
    g.DirectedLoadTemporary().DepthFirstSearchLinear()
    g.BreadthFirstSearch()

def double():
    l = List()
    for i in range(10):
        l.append(i)
    rich.print(f"[yellow]Length: {len(l)}")
    for i in l:
        rich.print(f"[red]{i}", end=",")
    print()
    l.insert(11)
    l.print()
    l.insert(12)
    l.print()
    RPanel.YellowBox(l.remove())
    l.print()
    l.pop()
    RPanel.RedBox(l.remove())
    RPanel.CyanBox(l.remove())
    l.pop()
    l.pop()
    l.print()


def main() -> None:

    arg = argument()
    if arg.FUNC == Func.stack:
        stack()
    elif arg.FUNC == Func.queue:
        queue()
    elif arg.FUNC == Func.graph:
        graph()
    elif arg.FUNC == Func.double:
        double()
    else:
        raise NotImplementedError("function not implemented")


if __name__ == "__main__":
    main()