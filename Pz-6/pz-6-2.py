#Дан список размера N. Найти номера тех элементов списка, которые больше своего
#правого соседа, и количество таких элементов. Найденные номера выводить в
#порядке их возрастания.
def find_elements(lst):
    indexes = []
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            indexes.append(i)
    return indexes, len(indexes)

my_list = [10, 5, 7, 0, 3, 2, 1, 11, 12]
result_indexes, result_count = find_elements(my_list)
print('Список:', my_list)
print("Номера элементов:", result_indexes)
print("Количество таких элементов:", result_count)