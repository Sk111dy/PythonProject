#______№1______

class Product:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available

    def __str__(self):
        status = "В наявності" if self.available else "Немає в наявності"
        return f"{self.name} — {self.price} грн ({status})"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product.available:
            self.products.append(product)
            print(f"Товар '{product.name}' додано до кошика")
        else:
            print(f"Товар '{product.name}' недоступний")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Товар '{product_name}' видалено з кошика")
                return
        print("Товар не знайдено у кошику")

    def total_price(self):
        return sum(product.price for product in self.products)

    def show_cart(self):
        if not self.products:
            print("Кошик порожній")
        else:
            print("Товари у кошику:")
            for product in self.products:
                print(product)
            print(f"Загальна вартість: {self.total_price()} грн")



#______№2______


class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Виконано" if self.completed else "Не виконано"
        return f"{self.title} | Дедлайн: {self.deadline} | Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Завдання '{task.title}' додано")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Завдання '{title}' видалено")
                return
        print("Завдання не знайдено")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Завдання '{title}' виконано")
                return
        print("Завдання не знайдено")

    def show_tasks(self):
        if not self.tasks:
            print("Список завдань порожній")
        else:
            print("Список завдань:")
            for task in self.tasks:
                print(task)




if __name__ == "__main__":

    p1 = Product("Ноутбук", 25000)
    p2 = Product("Мишка", 500)
    p3 = Product("Клавіатура", 1200, available=False)

    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)
    cart.show_cart()

    print("\n")


    manager = TaskManager()
    t1 = Task("Домашнє завдання", "Зробити ООП", "10.01.2026")
    t2 = Task("Прибрати кімнату", "Генеральне прибирання", "11.01.2026")

    manager.add_task(t1)
    manager.add_task(t2)
    manager.complete_task("Домашнє завдання")
    manager.show_tasks()
