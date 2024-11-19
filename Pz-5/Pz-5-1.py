#Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
#результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
#получится нуль?

def sum_digits(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digit_sum

def zero(n):
    count = 0
    while n != 0:
        n -= sum_digits(n)
        count += 1
    return count

a = input("Введите число - ")
while type(a) != int: # обработка исключений
   try:
    a = int(a)
   except ValueError:
    print("Неправильно ввели!")
    a = input("Введите число - ")


print("Через", zero(a), "действий получится ноль")
