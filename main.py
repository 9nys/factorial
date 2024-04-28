def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result_with_recursion = factorial(5)
print("Результат з рекурсією:", result_with_recursion)
