# Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится
# ли target в array. Такую процедуру будем называть поиском.
# Задача
# Реализовать императивную функцию поиска элементов на языке Python.


def find_target(arr, target):
    if target in arr:
        return arr[target]
    else:
        return None






if __name__ == '__main__':
    arr = [x for x in range(100)]
    target = 100

    print(find_target(arr, target))
