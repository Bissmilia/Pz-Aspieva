#Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в
#функции.
def schet():
 width = float(input('Введи ширину: '))
 height = float(input('Введи высоту: '))
 ploch = width * height
 perim = (width + height) * 2
 return ploch, perim
ploch_p, perim_p = schet()
print('Полощадь прямоугольника: ', ploch_p)
print('Периметр прямоугольника: ', perim_p)