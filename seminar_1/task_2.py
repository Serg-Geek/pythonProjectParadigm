# Условие
# На вход подается: список целых чисел arr
# ● Задача
# Реализовать императивную функцию, которая возвращает три числа:
# ○ Долю позитивных чисел
# ○ Долю нулей
# ○ Долю отрицательных чисел

def task_2(array):
    pos = 0
    zero = 0
    negative = 0
    for i in array:
        if i > 0:
            pos += 1
        if i < 0:
            negative += 1
        if i == 0:
            zero += 1
    print("pos=", pos/len(array))
    print("negative=", negative/len(array))
    print("zero=", zero/len(array))


if __name__ == "__main__":
    array = [-10,-11,16,17,0,0]
    task_2(array)



def task_2_1(array: list):
    total = len(array)
    pos = (sum(i > 0 for i in array))/total
    negative = (sum(i < 0 for i in array))/total
    zero  = (sum(i == 0 for i in array))/total
    
    print("pos=", pos)
    print("negative=", negative)
    print("zero=", zero)


if __name__ == "__main__":
    array = [-10,-11,16,17,0,0]
    task_2_1(array)


