#Дан символ C. Вывести его код (то есть номер в кодовой таблице).
# Ввод символа C
C = input("Введите символ: ")

# Получение кода символа
code = ord(C)

# Вывод кода символа
print(f"Код символа '{C}': {code}")