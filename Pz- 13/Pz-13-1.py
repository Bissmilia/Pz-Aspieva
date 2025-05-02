# Перенести в новый двумерный список Matr1 элементы,
# которые не находятся в первых и последних строках и столбцах
# матрицы Matr2 произвольного размера.

import random

rows = int(input('Введите количество строк: '))
cols = int(input('Введите количество столбцов: '))

matr2 = [[random.randint(-10, 20) for i in range(cols)] for i in range(rows)]
print('Исходная матрица: ')
for tabl in matr2:
    print(tabl)

matr1 = [row[1:-1] for row in matr2[1:-1]] if rows > 2 and cols > 2 else []
print('Новая матрица: ')
for tab in matr1:
    print(tab)
