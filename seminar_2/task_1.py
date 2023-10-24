


from string import ascii_uppercase, digits

DIGITS = digits + ascii_uppercase


def bin_octa(num, prod):
    result = []
    while num > 0:
        temp = num % prod
        result.append(DIGITS[temp])
        num //= prod
    return "".join(result[::-1])





if __name__ == '__main__':
    # rows = input("num_rows", int)
    # col = input("num_cols", int)
    res = 0
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    for i in range(len(matrix)):
       res += matrix[i][i]

    print("res" + str(res))


    decimal_number = 10
    binary_number = ''

    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2

    print(binary_number)  # Выводит '1010'


    DIGITS = digits + ascii_uppercase
    number = int(input("Введите число: "))
    res = bin_octa(number, 16)
    print(res)