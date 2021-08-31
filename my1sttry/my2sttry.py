def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def foo(x):
    fib(12.55)
    print(x)
