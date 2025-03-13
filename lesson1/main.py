# ex1

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Execution time: {elapsed_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

example_function(1000000)


# ex2
def cache_decorator(func):
    cashe = {}
    def wrapper(*args):
        if (args in cashe):
            return cashe[args]
        result = func(*args)
        cashe[args]=result
        return result
    return wrapper

@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print(fibonacci(10))
print(fibonacci(15))
print(fibonacci(15))