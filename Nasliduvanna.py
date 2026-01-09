#1
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Тварина видає звук")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # виклик конструктора батьківського класу
        self.breed = breed

    def speak(self):
        print(f"{self.name} каже: Гав!")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"{self.name} каже: Мяу!")


#2

class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Транспорт рухається зі швидкістю {self.speed} км/год")


class Car(Transport):
    def __init__(self, speed, fuel):
        super().__init__(speed)
        self.fuel = fuel

    def move(self):
        print(f"Автомобіль їде зі швидкістю {self.speed} км/год")


class Bicycle(Transport):
    def __init__(self, speed, type_bike):
        super().__init__(speed)
        self.type_bike = type_bike

    def move(self):
        print(f"Велосипед рухається зі швидкістю {self.speed} км/год")




if __name__ == "__main__":

    dog = Dog("Бобік", 4, "Лабрадор")
    cat = Cat("Мурка", 3, "Білий")

    dog.speak()
    cat.speak()

    print("\n")


    car = Car(120, "Бензин")
    bike = Bicycle(20, "Гірський")

    car.move()
    bike.move()
