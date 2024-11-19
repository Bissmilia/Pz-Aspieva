#Написать программу, подсчитывающую количество цифр числа, используя для
#этого функцию.
def count (s):
 a = 0
 while s > 0:
     s //= 10
     a += 1
 return a


number = input("Введи целое число: ")
while type(number) != int: # обработка исключений
 try:
     number = int(number)
 except ValueError:
     print("Неправильно ввели!")
     number = input("Введите целое число: ")

print('Количество цифр в цисле: ', count(number))