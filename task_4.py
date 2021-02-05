from sys import argv


# Задача 1
def zp():
    time, stavka, bonus = map(float, argv[1:])
    print(f'zp - {time * stavka + bonus}')


# Задача 2
list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
n = [list[m] for m in range(1, len(list))] if list[m] > list[m - 1]
print(n)
