class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0

    def show_speed(self):
        print(f"Поточна швидкість автомобіля {self.brand}: {self.speed} км/год")

car1 = Car("Toyota")


car1.show_speed()
car1.accelerate(50)
car1.show_speed()
car1.brake(20)
car1.show_speed()
car1.brake(50)
car1.show_speed()
