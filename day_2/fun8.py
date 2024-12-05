import time
import tracemalloc
import numpy as np

# pip install numpy

# tracemalloc.start()
# array1 = np.arange(10_000_000, dtype=np.int32)
array1 = np.arange(10_000_000)
# array2 = np.arange(10_000_000, dtype=np.int32)
array2 = np.arange(10_000_000)
print(array2.dtype)
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f'Current memory usage: {current / 1024 ** 2} MB')
# print(f'Peak memory usage: {peak / 1024 ** 2} MB')
# Current memory usage: 152.58807373046875 MB
# Peak memory usage: 152.58807373046875 MB
# int32
# Current memory usage: 76.29422187805176 MB
# Peak memory usage: 76.29467487335205 MB

# tracemalloc.start()
list1 = list(range(10_000_000))
list2 = list(range(10_000_000))


# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f'Current memory usage: {current / 1024 ** 2} MB')
# print(f'Peak memory usage: {peak / 1024 ** 2} MB')
# Current memory usage: 762.9238739013672 MB
# Peak memory usage: 762.9239807128906 MB

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(F"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def add_without_np():
    res = [list1[i] + list2[i] for i in range(len(list1))]
    return "OK"


@measure_time
def add_np():
    res = array1 + array2
    return "OK Np"

@measure_time
def add_zip():
    res = [a + b for a, b in zip(list1, list2)]
    return "OK zip"

5
print("Start")
print(add_without_np())
print(add_np())
print(add_zip())
# Czas wykonania funkcji add_without_np: 1.4444034099578857
# OK
# Czas wykonania funkcji add_np: 0.05009579658508301
# OK Np
