def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factor(n - 1)
