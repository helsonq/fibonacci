def fibonacci(n):
    fib = [0, 1]  # Первые два числа

    if n <= 0:
        return []
    elif n == 1:
        return [0]

    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


# Генерация списка из 100 чисел
fib_100 = fibonacci(100)

# Проверка (вывод первых 10 элементов)
print("Первые 10 чисел Фибоначчи:", fib_100[:10])