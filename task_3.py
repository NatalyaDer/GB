# Задача 1

def fun(n, m):
    if m >= 0:
        n = int(input('n: '))
        m = int(input('m: '))
        num = n / m
        print(num)
    elif m < 0:
        print('Делить на ноль нельзя')
    else:
        print('None')


fun(4, 5)


# Задача 2

def person(name, surname, birthday, city, emaile, phone):
    return f'Name - {name}, Surname - {surname}, Birthday - {birthday}, City - {city}, Emaile - {emaile}, Phone - {phone}'


print(person(name='Nata', surname='Der', birthday='26.01.1990', city='Seversk', emaile='njnj@jh.com', phone='222652'))

# Задача 3

def my_func(a,b,c):
    list = [a,b,c]
    list.remove(min(list))
    print(sum(list))

my_func(4,3,1)

#Задача 4

def stepen(x, y):
    s = x ** y
    print(s)


stepen(4, -5)

# Задача 5
# Задача 6
# Задача 7
