from functools import lru_cache
from tree import SplayTree
import timeit
from rich.console import Console
from rich.table import Table
import matplotlib.pyplot as plt


@lru_cache(maxsize=500)
def fibonacci_lru(n: int):
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def fibonacci_splay(n: int, tree: SplayTree):
    if n < 2:
        return n
    cached = tree.find(n)
    if cached:
        return cached
    result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, result)
    return result

requested_fibonacci_numbers = [x for x in range(0, 951, 50)]
print(f"Requested Fibonacci numbers: {requested_fibonacci_numbers}")

def display_comparison(timings):
    console = Console()

    table = Table(title="LRU Cache та Splay Tree performance comparison", show_header=True, header_style="bold magenta")

    table.add_column("n", justify="center", style="bold")
    table.add_column("LRU Cache Time (s)", justify="center", style="bold")
    table.add_column("Splay Tree Time (s)", justify="center", style="bold")

    for n, (lru_time, splay_time) in timings.items():
        table.add_row(f"[dim]{n}[/dim]", f"[dim]{lru_time:.8f}[/dim]", f"[dim]{splay_time:.8f}[/dim]")

    console.print(table)

def draw_graph(timings):
    fibanachi_numbers = list(timings.keys())
    lru_results = [x[0] for x in timings.values()]  # LRU Cache
    splay_results = [x[1] for x in timings.values()]  # Splay Tree

    plt.plot(fibanachi_numbers,lru_results,"-o",label="LRU Cache",)
    plt.plot(fibanachi_numbers, splay_results, "-o", label="Splay Tree")
    plt.xlabel("Fibanacci number (n)")
    plt.ylabel("Average time (seconds)")
    plt.title("LRU Cache та Splay Tree performance comparison")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.show()

timings = {}
splay_tree = SplayTree()
for n in requested_fibonacci_numbers:
    lru = timeit.timeit(lambda: fibonacci_lru(n), number=10)
    splay = timeit.timeit(lambda: fibonacci_splay(n, splay_tree), number=10)
    timings[n] = (lru, splay)

display_comparison(timings)
draw_graph(timings)
