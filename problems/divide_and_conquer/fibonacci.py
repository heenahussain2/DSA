def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


for i in range(9):
    print(fibonacci_recursive(i), end=" ")
