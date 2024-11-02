# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2

a = input("Введи число 1") # Ввод данных
b = input("Введи число 2")

while type(a) != int: # обработка исключений
 try:
  a = int(a)
 except ValueError:
  print("Неправильно ввели!")
  b = input('Введите число 1')
while type(b) != int: # обработка исключений
 try:
  b = int(b)
 except ValueError:
  print("Неправильно ввели!")
  b = input('Введите число 2')

c = a + b
if c % 5 == 0:
  c = c + 1
else:
  c = c - 2
print(c)