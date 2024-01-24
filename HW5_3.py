# 4. Создайте функцию генератор чисел Фибоначчи
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

def fibonaci0(N: int):
    list_fib = [0, 1]
    yield list_fib[0]
    yield list_fib[1]
    for i in range(2,N):
        list_fib.append(list_fib[i-1] + list_fib[i-2])
        yield list_fib[i]


def fibonaci1(N: int):
    fib1 = 0
    fib2 = 1
    yield  fib1
    yield  fib2
    i = 2
    while i < N:
        sum = fib1 + fib2
        fib1 = fib2
        fib2 = sum
        i += 1
        yield fib2



print(*fibonaci0(10))

for num in fibonaci1(10):
    print(num)