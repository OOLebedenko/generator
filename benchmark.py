import math
import time


def benchmark_infit_generator(func, replication=1000):
    start = time.time()
    generator = func()
    for i in range(replication):
        (next(generator))
    end = time.time()
    print(end - start)
    return func


def primes_wilson_theorem():
    a = 1
    while True:
        a += 1
        if (math.factorial(a - 1) + 1) % a == 0:
            yield a


def primes_optimization():
    i = 1
    while True:
        count = 0
        if i <= 2:
            i += 1
        else:
            i += 2
        for k in range(2, int(i ** 0.5) + 1):
            if i % k == 0:
                count += 1
                break
        if count == 0:
            yield i


if __name__ == '__main__':
    benchmark_infit_generator(primes_wilson_theorem)
    benchmark_infit_generator(primes_optimization)
