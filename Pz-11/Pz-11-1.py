# Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Отрицательные нечетные элементы:
# Сумма отрицательных нечетных элементов:
# Среднее арифметическое отрицательных нечетных элементов:

numbers = ['-2 -3 10 -12 64 2 -9 8 -3 15 32 -7']
f1 = open('text.txt', 'w', encoding='utf-8')
f1.writelines(numbers)
f1.close()

f2 = open('text_2.txt', 'w', encoding='utf-8')
f2.write('Исходные данные: ')
f2.writelines(numbers)
f2.close()

f1 = open('text.txt')
k = f1.read().split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

otr_odd = [x for x in k if x < 0 and x % 2 != 0]
s = sum(otr_odd)
avg = s / len(otr_odd) if otr_odd else 0

f2 = open('text_2.txt', 'a', encoding='utf-8')
print('Количество элементов:', len(k), file=f2)
print('Отрицательные нечетные элементы:', ' '.join(map(str, otr_odd)), file=f2)
print('Сумма отрицательных нечетных элементов:', s, file=f2)
print('Среднее арифметическое отрицательных нечетных элементов:', round(avg, 2), file=f2)
f2.close()
