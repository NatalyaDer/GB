# Задача 1

a = input('Enter your age:')  # строка
b = int(input('Enter your age:'))  # число
print(a, b)

# Задача 2
clock = int(input('Сколько времени в секундах?'))
hour = clock // 3600
minute = (clock // 60) - (hour * 60)
second = clock % 60
print(f'{hour:02}:{minute:02}:{second:02}')

# Задача 3
n = input(" Введи число: ")
print(f'{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}')


