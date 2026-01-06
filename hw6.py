#1
class Character:
    def __init__(self, name, health):
        self.__name = name
        self.__health = max(0, health)  # захист від негативного здоров'я

    def attack(self):
        print("Персонаж атакує")

    def take_damage(self, amount):
        if amount < 0:
            return
        self.__health = max(0, self.__health - amount)

    def is_alive(self):
        return self.__health > 0

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 150)

    def attack(self):
        print(f"{self.get_name()} атакує мечем")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 100)

    def attack(self):
        print(f"{self.get_name()} атакує магією")


# Приклад використання
warrior = Warrior("Артур")
mage = Mage("Мерлін")

warrior.attack()
mage.attack()

mage.take_damage(30)
print("Маг живий?", mage.is_alive())

#2
class LibraryItem:
    def __init__(self, title, author, item_id):
        self._title = title
        self._author = author
        self._item_id = item_id

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_item_id(self):
        return self._item_id

    def display_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages):
        super().__init__(title, author, item_id)
        self._pages = pages

    def display_info(self):
        print(f"Книга: {self._title}, Автор: {self._author}, Сторінки: {self._pages}")


class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self._issue_number = issue_number

    def display_info(self):
        print(f"Журнал: {self._title}, Автор: {self._author}, Номер випуску: {self._issue_number}")


class Audiobook(LibraryItem):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self._duration = duration

    def display_info(self):
        print(f"Аудіокнига: {self._title}, Автор: {self._author}, Тривалість: {self._duration} хвилин")


library_items = [
    Book("1984", "Джордж Орвелл", 1, 328),
    Magazine("National Geographic", "Редакція", 2, 202),
    Audiobook("Гаррі Поттер", "Дж. К. Ролінґ", 3, 600)
]

print("\nІнформація про матеріали бібліотеки:")
for item in library_items:
    item.display_info()