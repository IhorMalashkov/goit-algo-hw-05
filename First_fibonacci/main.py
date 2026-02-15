def caching_fibonacci():
    cache = {} #Створення порожнього списку
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache: #Перевірка наявності значення в кеші
            return cache[n]
        cache[n]=fibonacci(n-1) + fibonacci(n-2) # Якщо немає в кеші, обчислюємо рекурсивно і записуємо в кеш
        return cache[n]
    return fibonacci

fib = caching_fibonacci()# Отримуємо функцію fibonacci

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))
print(fib(15))
