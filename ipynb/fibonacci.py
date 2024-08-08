def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fiblist(n):
    fibonacci_list = [0, 1]
    for i in range(1, n):
        fibonacci_list += [fibonacci_list[-1] + fibonacci_list[-2]]
    return fibonacci_list
