# # Наслідування, інкапсуляція (public, private, protected), поліморфізм
#
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         pass
#         #print("\nІнформація про студека який навчається у вищому освітньому закладі\nІм'я: ", self.name, "\nВік: ",self.age)
#
# class studentSchool(Student):
#             def __init__(self, name, age, school):
#                 super().__init__(name, age)
#                 self.school = school
#
#             def info(self):
#                 print("У школі", self.school)
#
# class studentUneversity(Student):
#     def __init__(self, name, age, nameUneversity):
#         super().__init__(name, age)
#         self.nameUneversity = nameUneversity
#     def info(self):
#         print("Назва спеціальності", self.nameUneversity)
#
#
# #st = Student("Світлана", 20)
# #st.info()
# stud=[
# studentUneversity("Сашко","20", "Розробник"),
# studentSchool("Глаша","11","93"),
# Student("Гріша","4"),
# ]
#
# for s in stud:
#     print(s.name, s.age)
#     s.info()
#
# class Dani:
#     def __init__(self, password):
#         self.__password = password
#
#     def changePass(self,value):
#         return self.__password == value
#
#
# d1 = Dani("123")
# print(d1.changePass("123456")) #Напряму захищені дані не можна викликати
# print(d1._Dani__password)

#людина, учень (серед бал), робітник (ЗП)

class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def info(self):
        print("Ім'я: ", self.__name, "\nВік: ", self.__age)
    def old(self):
        return self.__age>17

class School(Human):
    def __init__(self, name, age, clas, ball):
        super().__init__(name, age)
        self.clas = clas
        self.__ball = ball
    def grade(self):
        return sum(self.__ball)/len(self.__ball)
    def info(self):
        super().info()
        print("Середній бал учня:", self.grade())
class Worker(Human):
    def __init__(self, name, age, stavka, hour):
        super().__init__(name, age)
        self.__stavka = stavka
        self.hour = hour
    def salary(self):
        return self.__stavka*self.hour
    def info(self):
        super().info()
        print("Зарплатня: ", self.salary())

people=[
    School("Оля", 15, 9, [11, 7, 9, 10]),
    School("Петя", 18, 11, [9, 11, 5, 10]),
    Worker("Леана", 32, 175.50, 50),
    Worker("Андрій", 22, 190, 85),
]

for p in people:
    p.info()
    print("Повнолітні: ", p.old(), "\n")