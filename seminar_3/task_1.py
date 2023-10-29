# Контекст
# Предположим, что мы хотим написать программу для исследования геометрических фигур. Для того
# чтобы это сделать мы решили начать с создания абстрактного класса - “Фигура”.
# ● Задача
# Реализовать класс Shape, содержащий пустые методы get_area и get_perimeter. Использовать библиотеку
# абстрактных классов “ABC” в данном случае - не обязательно
#
# 2Контекст
# Теперь, когда у вас есть абстрактный класс Shape, ваша следующая задача - получить класс Circle.
# ● Задача
# Реализовать дочерний от Shape класс Circle, включая следующие работающие методы:
# ○ конструктор класса __init__ - метод инициализации класса Circle.
# ○ get_area - метод для расчета площади круга
# ○ get_perimeter - метод для расчета периметра окружности

# 3Контекст
# И наконец, последняя задача - по аналогии с кругом создать класс для треугольника и расчета его
# характеристик.
# ● Задача
# Реализовать дочерний от Shape класс Triangle, включая следующие работающие методы:
# ○ конструктор класса __init__ - метод инициализации класса.
# ○ get_area - метод для расчета площади
# ○ get_perimeter - метод для расчета периметра


import math

class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 *math.pi * self.radius

class Triangle_right(Shape):
    def __init__(self, catet_a, catet_b):
        self.catet_a = catet_a
        self.catet_b = catet_b
        self.gipotenuza = ((catet_a ** 2) + (catet_b ** 2)) ** 0.5
    def get_perimeter(self):
        return self.catet_a + self.catet_b + self.gipotenuza


    def get_area(self):
        return (self.catet_a * self.catet_b) / 2

if __name__ == '__main__':
    tr = Triangle_right(5,5)
    print(f'{tr.get_area()= }, {tr.get_perimeter()= }')


