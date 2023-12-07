import doctest
from typing import Union


class Car:
    def __init__(self, price: float, max_speed: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param price: Цена автомобиля
        :param max_speed: Маскимальная скорость автомобиля

        Примеры:
        >>> BMW = Car(6000000, 500)  # инициализация экземпляра класса
        """
        self.current_speed = 0
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        if price < 0:
            raise ValueError("Цена должна быть положительным числом")
        self.price = price

        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть типа int или float")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость не может быть отрицательным числом или раняться нулю")
        self.max_speed = max_speed

    def init_speed(self, initial_speed: float) -> None:
        """

        Функция задающая начальную скорость автомобиля

        :param initial_speed: Разица между начальной и конечной скоростями
        :raise ValueError: Если начальную скорость не яляется int или float, то вызываем ошибку
        :raise ValueError: Если начальную скорость является отрицательным числом, то вызываем ошибку

        Примеры:
        >>> BMW = Car(6000000, 500)  # инициализация экземпляра класса
        >>> BMW.init_speed(30) # вызов функции
        """
        if not isinstance(initial_speed, (int, float)):
            raise TypeError("Начальную скорость должна быть типа int или float")
        if initial_speed < 0:
            raise ValueError("Начальную скорость не может быть отрицательным числом или раняться нулю")
        self.current_speed = initial_speed

    def to_current_speed(self, increase: int) -> None:
        """

        Функция увелиивающая текущую скоость автомобиля

        :param increase: Разица между начальной и конечной скоростями
        :raise TypeError: Если добавочая скорость не яляется int или float, то вызываем ошибку
        :raise ValueError: Если добавочая скорость является отрицательным числом, то вызываем ошибку.Также, нельзя певышать максимальную скорость

        Примеры:
        >>> BMW = Car(6000000, 500)  # инициализация экземпляра класса
        >>> BMW.init_speed(30) # вызов функции начальной скорости
        >>> BMW.to_current_speed(3) #вызов функции уеличения скорости
        """
        if not isinstance(increase, int):
            raise TypeError("Добавочая скорость должна быть типа int или float")
        if increase < 0 or self.current_speed + increase > self.max_speed:
            raise ValueError(
                "Добавочая скорость не может быть отрицательным числом или раняться нулю. Также, нельзя певышать максимальную скорость")
        self.current_speed += increase
        # while self.current_speed != self.current_speed + increase:
        #     self.current_speed += 1

    def cur_speed(self) -> float:
        """
        Функция, возвращающая текущую скорость
        >>> BMW = Car(6000000, 500)  # инициализация экземпляра класса
        >>> BMW.init_speed(30) # вызов функции начальной скорости
        >>> BMW.to_current_speed(3) # вызов функции уеличения скорости
        >>> BMW.cur_speed() # вызов функции отображения текущей скорости
        33

        """
        return self.current_speed


class Tree:
    condition = ("green", "gold", "gray")
    def __init__(self, name: str, color: str, seeds: float):
        """
        :param seeds: количетво семян
        :param name: Название дерева
        :param color: Цвет дерева
        :raise TypeError: Если название дерева не яляется str, то вызываем ошибку
        :raise TypeError: Если цвет дерева не яляется str, то вызываем ошибку

        """
        self.seeds = 0
        self.generate_seeds(seeds)
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        self.name = name

        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        self.color = color
        if color not in self.condition:
            raise TypeError("Введите определенный цвет")

    def change_color(self, color: str) -> None:
        """
        Функция которая меняет цвет дерева
        :raise TypeError: Если новый цвет дерева не яляется str, то вызываем ошибку
        :raise TypeError: Если новый цвет дерева не входит в condition, то вызываем ошибку
        Примеры:
        >>> a = Tree("oak", "green", 3.0000)
        >>> a.change_color("gold")

        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        if color not in self.condition:
            raise TypeError("Введите определенный цвет")
        self.color = color


    def generate_seeds(self, seeds: float) -> None:
        """
        Функция которая меняет цвет дерева
        :raise TypeError: Если seeds не float
        :raise ValueError: Если seeds является отрицательным числом, то вызываем ошибку.
        Примеры:

        >>> oak = Tree("oak", "green", 3.00)

        """
        if not isinstance(seeds, float):
            raise TypeError("Семена должны быть float")
        if seeds < 0:
            raise ValueError("Семяна является отрицательным числом")





class Im_number:
    def __init__(self, real_part: Union[int, float], im_part: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Комплексное число"

        :param real_part: Цена автомобиля
        :param im_part: Маскимальная скорость автомобиля
        :raise TypeError: Если реальная часть числа является типом отличным от int или float , то вызываем ошибку.
        :raise TypeError: Если мнимая часть числа является типом отличным от int или float , то вызываем ошибку.
        Примеры:
        >>> first = Im_number(6, 50)  # инициализация экземпляра класса
                """
        if not isinstance(real_part, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        self.real = real_part
        if not isinstance(im_part, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        self.im = im_part

    def __add__(self, other: "Im_number") -> "Im_number" :
        """
        Функция сложения двух комплексных чисел
        :param other: Комплексное число
        Примеры
        >>> first = Im_number(6, 50)
        >>> second = Im_number(6, 50)
        >>> fird = first + second

        """
        return Im_number(self.real+other.real, self.im+other.im)

    def show(self) -> None:
        """
        Функция вывода комплексного числа в консоль
        Пример:
        >>> first = Im_number(6, 50)
        >>> first.show()
        6 + i50
        """
        if self.im >= 0:
            print(f"{self.real} + i{self.im}")
        else:
            print(f"{self.real} - i{abs(self.im)}")



if __name__ == "__main__":
    doctest.testmod()

