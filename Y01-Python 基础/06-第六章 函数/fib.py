def fib():
    a = 0
    b = 1
    while a < 100:
        print(a)
        a, b = b, a+b


if __name__ == '__main__':
    fib()
