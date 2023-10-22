# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i -1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j+1], array[j]
    return array

def sort_list_declarative(array):
    return sorted(array, reverse=True)



if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    print("императивный стиль ",  sort_list_imperative(array))
    print("декларативвый стиль ", sort_list_declarative(array))



