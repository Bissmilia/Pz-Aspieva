#Дан список A размера N и целые числа K и L (1 < K < L < N). Переставить в обратном
#порядке элементы списка, расположенные между элементами AK и AL, не включая
#эти элементы.

def reverse_between(arr, k, l):
    # Извлечение между K и L
    subarray = arr[k + 1:l]
    subarray.reverse()  # Переворот списка

    # Замена в оригинальном списке
    arr[k + 1:l] = subarray
    return arr


# Пример списка и ввода K и L
A = [10, 20, 30, 40, 50, 60, 70, 80, 90]
N = len(A)

# Ввод значений K и L
K = input(f"Введите K (1 < K < {N - 1}): ")
L = input(f"Введите L (K < L < {N}): ")

while type(K) != int: # обработка исключений
   try:
    K = int(K)
   except ValueError:
    print("Неправильно ввели!")
    K = input(f"Введите K (1 < K < {N - 1}): ")
while type(L) != int: # обработка исключений
   try:
    L = int(L)
   except ValueError:
    print("Неправильно ввели!")
    L = input(f"Введите L (K < L < {N}): ")

print("Исходный список:", A)

# Перестановка и вывод результата
result = reverse_between(A, K, L)
print("Список после перестановки:", result)