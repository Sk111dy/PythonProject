import random as r

class Student:
    def __init__(self, name):
        self.name = name
        self.progress = r.randint(40, 70)
        self.happy = r.randint(40, 70)
        self.money = r.randint(50, 150)
        self.life = True

    def study(self):
        print("Студент навчається")
        self.progress += r.randint(5, 15)
        self.happy -= r.randint(3, 8)
        self.money -= 5

    def sleep(self):
        print("Студент спить")
        self.happy += r.randint(5, 10)

    def chill(self):
        print("Студент відпочиває")
        self.happy += r.randint(5, 10)
        self.money -= r.randint(5, 15)

    def work(self):
        print("Студент працює")
        self.money += r.randint(20, 40)
        self.happy -= r.randint(5, 10)

    def is_alive(self):
        if self.progress < 30:
            print(self.name, "відрахований з навчання")
            self.life = False
        elif self.happy <= 0:
            print(self.name, "у депресії та кидає навчання")
            self.life = False
        elif self.money < -50:
            print(self.name, "не має грошей для життя")
            self.life = False

    def show_stats(self, day):
        print(f"""
День {day}
Щастя: {self.happy}
Успішність: {self.progress}
Гроші: {self.money}
""")

    def live_day(self, day):
        print("=" * 30)

        # Розумна поведінка
        if self.money < 20:
            self.work()
        elif self.progress < 60:
            self.study()
        elif self.happy < 40:
            self.sleep()
        else:
            r.choice([self.study, self.chill, self.sleep])()

        self.show_stats(day)
        self.is_alive()


student = Student("Вася")

for day in range(1, 366):
    if not student.life:
        break
    student.live_day(day)

print("Симуляція завершена")
