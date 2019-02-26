def fib():
    fib_0, fib_1 = 0, 1
    while True:
        fib_0, fib_1 = fib_1, fib_1 + fib_0
        yield fib_0


if __name__ == "__main__":
    g = fib()
    for i in range(6):
        print(next(g))
