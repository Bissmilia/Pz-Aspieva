# Даны координаты точки, не лежащей на координатных осях OX и OY. Определить номер координатной четверти, в которой находится данная точка.

x = input("Введите точку координат X") #Ввод данных
y = input("Введите точку координат Y")

while type(x) != int: # обработка исключений
 try:
  x = int(x)
 except ValueError:
  print("Неправильно ввели!")
  x = input("Введите точку координат X")

while type(y) != int: # обработка исключений
 try:
  y = int(y)
 except ValueError:
  print("Неправильно ввели!")
  y = input("Введите точку координат Y")

if x > 0 and y > 0: #Определяем номер кординатной четверти
  print ('номер координатной четверти - 1')
elif x < 0 and y > 0:
  print('номер координатной четверти - 2')
elif x == 0 and y == 0:
  print('Начало координат')
elif x < 0 and y < 0:
  print('номер координатной четверти - 3')
else:
  print('номер координатной четверти - 4')

