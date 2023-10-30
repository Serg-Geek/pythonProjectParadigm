# Контекст
# Корреляция - статистическая мера, используемая для оценки
# связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.


import math

def calculate_mean(arr):
    """Функция для вычисления среднего значения массива"""
    return sum(arr) / len(arr)

def calculate_covariance(arr1, arr2):
    """Функция для вычисления ковариации между двумя массивами"""
    mean_arr1 = calculate_mean(arr1)
    mean_arr2 = calculate_mean(arr2)
    covariance = sum([(arr1[i] - mean_arr1) * (arr2[i] - mean_arr2) for i in range(len(arr1))])
    return covariance

def calculate_standard_deviation(arr):
    """Функция для вычисления стандартного отклонения массива"""
    mean = calculate_mean(arr)
    variance = sum([(x - mean) ** 2 for x in arr]) / len(arr)
    return math.sqrt(variance)

def calculate_pearson_correlation(arr1, arr2):
    """Функция для вычисления корреляции Пирсона между двумя массивами"""
    covariance = calculate_covariance(arr1, arr2)
    std_deviation_arr1 = calculate_standard_deviation(arr1)
    std_deviation_arr2 = calculate_standard_deviation(arr2)

    if std_deviation_arr1 != 0 and std_deviation_arr2 != 0:
        correlation = covariance / (std_deviation_arr1 * std_deviation_arr2)
        return correlation
    else:
        return 0  # В случае, если одно из стандартных отклонений равно нулю


if __name__ == '__main__':
    array1 = [1, 2, 3, 4, 5]
    array2 = [2, 4, 6, 8, 10]

    correlation = calculate_pearson_correlation(array1, array2)
    print(f"Корреляция Пирсона: {correlation}")
