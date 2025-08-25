# --------------------------------------------------------------------- #
# IMPORTS
# --------------------------------------------------------------------- #

import tracemalloc
from timeit import timeit
import statistics

# --------------------------------------------------------------------- #
# FUNCTIONS TO COMPARE
# --------------------------------------------------------------------- #

def func_1():
    items = []
    for i in range(100):
        items.append(i)


def func_2():
    items = [i for i in range(100)]

# --------------------------------------------------------------------- #
# SETTINGS
# --------------------------------------------------------------------- #

ITER_MEM  = 100
ITER_TIME = 1000

# --------------------------------------------------------------------- #
# MEASUREMENT
# --------------------------------------------------------------------- #

def measure(func):
    mem_samples = []

    # Warm-up tracemalloc
    tracemalloc.start()
    tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Memory measurements
    for _ in range(ITER_MEM):
        tracemalloc.start()
        func()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        mem_samples.append(peak)

    avg_bytes = statistics.mean(mem_samples)
    stdev_bytes = statistics.stdev(mem_samples) if len(mem_samples) > 1 else 0.0

    # Time measurement
    total_time = timeit(func, number=ITER_TIME)

    return avg_bytes, stdev_bytes, total_time

# --------------------------------------------------------------------- #
# OUTPUT
# --------------------------------------------------------------------- #

def print_results(index, name, avg_bytes, stdev_bytes, total_time):
    kb = avg_bytes / 1024
    mb = kb / 1024
    gb = mb / 1024
    print(f"| {index:>3} | {name:<12} | {int(avg_bytes):>10,} | {kb:>10.3f} | {mb:>10.3f} | {gb:>10.6f} | ±{stdev_bytes:>9.1f} | {total_time:>10,.6f} | {ITER_TIME:>10,} |")

# --------------------------------------------------------------------- #
# MAIN
# --------------------------------------------------------------------- #

if __name__ == "__main__":

    print(f"|{'-'*115}|")
    print(f"| {'#':^3} | {'Function':^12} | {'Bytes':^10} | {'KB':^10} | {'MB':^10} | {'GB':^10} | {'Std Dev':^11} | {'Time':^10} | {'Iter':^10} |")
    print(f"|{'-'*115}|")

    funcs = [func_1, func_2]
    for index, func in enumerate(funcs, start=1):
        avg_bytes, stdev_bytes, total_time = measure(func)
        print_results(index, func.__name__, avg_bytes, stdev_bytes, total_time)
