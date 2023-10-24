#● Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# ● Пример вывода:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9



def multiplication_table(num):
    START = 1
    END = 10
    HALF = 2

    for i in range(START, END):
        for j in range(START, (num+1) // HALF + 1):
            print(f"{j:>2} X {i:>1} = {i * j:>2}", end="   ")
        print()
    print()
    for i in range(START, END):
        for j in range(5 // HALF + 1, num + 1):
            print(f"{j:>2} X {i:>1} = {i * j:>2}", end="   ")
        print()


if __name__ == '__main__':
    n = int(input("Введите число n: "))
    multiplication_table(n)

