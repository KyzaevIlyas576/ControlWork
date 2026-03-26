from abc import ABC, abstractmethod
import math


# 1) Инкапсуляция
class Person:
    def __init__ (self, name):
        self.name = name
        self.__age = int()


    # @property
    # def age(self):
    #     return self.__age
    #
    # @age.setter
    # def age(self, age):
    #     self.__age = age


    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
            print(f"Возраст: {age}")
        else:
            # self.__age = abs(age)
            raise ValueError("Возраст не может быть отрицательным.")


p = Person(name="Алекс")
p.set_age(25)               # 25
print(p.get_age())
# p.set_age(-5)             # ошибка


# 2) Полиморфизм
class Animal:
    def __init__(self, name):
        self.name = name


    def speak(self):
        return f"{self.name}: I am an animal."


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


    def speak(self):
        return f"{self.name}: Woof."


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)


    def speak(self):
        return f"{self.name}: Meow."


dog = Dog("Buddy")
cat = Cat("Kitty")
print(dog.speak())      # Buddy: Woof
print(cat.speak())      # Kitty: Meow
print()


# 3) Полиморфизм
class Vehicle:
    # def __init__(self, name):
    #     self.name = name


    def move(self):
        return f"Vehicle is moving."


class Car(Vehicle):
    # def __init__(self, name):
    #     super().__init__(name)
    #     self.name = name


    def move(self):
        return f"Car is driving."


class Bicycle(Vehicle):
    # def __init__(self, name):
    #     super().__init__(name)
    #     self.name = name


    def move(self):
        return f"Bicycle is pedaling."


def move(vehicle):
    return vehicle.move()


car = Car()
bike = Bicycle()
print(move(car))
print(move(bike))
print()


# 4) Абстракция
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"{(round(float(math.pi * self.radius ** 2)))}"


rect = Rectangle(10, 5)
circle = Circle(7)
print(rect.area())          # Вывод: 50
print(circle.area())        # Вывод: ~154
