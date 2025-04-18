# Из предложенного текстового файла (text18-1.txt) вывести на экран его содержимое,
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку между первой и второй.

f1 = open('text18-1.txt', 'r', encoding='utf-16')
lines = f1.readlines()
text = ''.join(lines)
count = 0
for char in text:
    if char.isupper():
        count += 1
print('Содержимое файла:\n', text)
print('Количество букв в верхнем регистре:', count)
f1.close()

f2 = open('text18-2.txt', 'w', encoding='utf-16')
f2.write(lines[0])
f2.write(lines[-1])
f2.write(lines[1])
for i in range(2, len(lines) - 1):
        f2.write(lines[i])
print('Количество букв в верхнем регистре:', count, file=f2)
f2.close()

