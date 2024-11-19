#Описать функцию PowerA234(параметры), вычисляющую вторую, третью и
#четвертую степень числа A и возвращающую эти степени соответственно в
#переменные B, C и D. С помощью этой функции найти вторую, третью и четвертую
#степень пяти данных чисел.
def PowerA234(A):
    B = A ** 2  # Вычисляем вторую степень
    C = A ** 3  # Вычисляем третью степень
    D = A ** 4  # Вычисляем четвертую степень
    return B, C, D


# Первое число
number1 = input('Введите первое число: ')
while type(number1) != int:  # обработка исключений
    try:
        number1 = int(number1)
    except ValueError:
        print("Неправильно ввели!")
        number1 = int(number1)
B1, C1, D1 = PowerA234(number1)

print(f'Число: {number1}, 2 степень: {B1}, 3 степень: {C1}, 4 степень: {D1}')
# Второе число
number2 = int(input('Введите второе число: '))
while type(number2) != int: # обработка исключений
   try:
     number2 = int(number2)
   except ValueError:
    print("Неправильно ввели!")
    number2 = int(number2)
B2, C2, D2 = PowerA234(number2)
print(f'Число: {number2}, 2 степень: {B2}, 3 степень: {C2}, 4 степень: {D2}')
# Третье число
number3 = int(input('Введите третье число: '))
while type(number3) != int: # обработка исключений
   try:
     number3 = int(number3)
   except ValueError:
    print("Неправильно ввели!")
    number3 = int(number3)
B3, C3, D3 = PowerA234(number3)
print(f'Число: {number3}, 2 степень: {B3}, 3 степень: {C3}, 4 степень: {D3}')
# Четвертое число
number4 = int(input('Введите четвертое число: '))
while type(number4) != int: # обработка исключений
   try:
     number4 = int(number4)
   except ValueError:
    print("Неправильно ввели!")
    number4 = int(number1)
B4, C4, D4 = PowerA234(number4)
print(f'Число: {number4}, 2 степень: {B4}, 3 степень: {C4}, 4 степень: {D4}')
# Пятое число
number5 = int(input('Введите пятое число: '))
while type(number5) != int: # обработка исключений
   try:
     number5 = int(number5)
   except ValueError:
    print("Неправильно ввели!")
    number5 = int(number5)
B5, C5, D5 = PowerA234(number5)
print(f'Число: {number5}, 2 степень: {B5}, 3 степень: {C5}, 4 степень: {D5}')