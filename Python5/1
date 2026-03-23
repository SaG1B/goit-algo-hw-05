def caching_fibonacci():
    cache = {}  # кеш для збереження значень

    def fibonacci(n):
        # базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # якщо вже рахували — беремо з кешу
        if n in cache:
            return cache[n]

        # рахуємо рекурсивно і зберігаємо
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci


# =====================
# ПРИКЛАД ВИКОРИСТАННЯ
# =====================

fib = caching_fibonacci()

print(fib(10))  # 55
print(fib(15))  # 610