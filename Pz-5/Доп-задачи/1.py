#Даны три целых числа. Определить у какого числа больше сумма цифр. Вывод
#результата предусмотреть в основной программе. Расчет суммы цифр оформить в
#функции.
def sum_of_digits(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digit_sum
# Ввод трех целых чисел
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

# Вычисление суммы цифр для каждого числа
sum1 = sum_of_digits(num1)
sum2 = sum_of_digits(num2)
sum3 = sum_of_digits(num3)
# Определение числа с наибольшей суммой цифр
if sum1 > sum2 and sum1 > sum3:
    result = f"У первого числа {num1} сумма цифр больше: {sum1}."
elif sum2 > sum1 and sum2 > sum3:
    result = f"У второго числа {num2} сумма цифр больше: {sum2}."
elif sum3 > sum1 and sum3 > sum2:
    result = f"У третьего числа {num3} сумма цифр больше: {sum3}."
else:
    result = "Суммы цифр у чисел равны."

# Вывод результата
print(result)