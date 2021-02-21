# Factorial Function

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)\

def factorial_no_recur(n):
    val = 1
    for i in range(1, n + 1):
        val *= i
    return val

# real simplest way would be using math lib factorial import function