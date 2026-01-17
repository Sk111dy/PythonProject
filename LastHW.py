import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = []

items = soup.select("article.product_pod")[:10]

for item in items:
    name = item.h3.a["title"]

    price_text = item.select_one("p.price_color").text
    price_text = "".join(ch for ch in price_text if ch.isdigit() or ch == ".")
    price = float(price_text) * 50  # грн

    products.append({
        "name": name,
        "price": round(price)
    })

print("ТОП-10 товарів:\n")
for i, product in enumerate(products, 1):
    print(f"{i}. {product['name']} - {product['price']} грн")

cart = []
total_sum = 0

while True:
    choice = int(input("\nЯкий товар ви хочете придбати? (введіть номер): "))
    quantity = int(input("Скільки одиниць ви хочете купити?: "))

    selected = products[choice - 1]
    cost = selected["price"] * quantity

    cart.append((selected["name"], quantity, cost))
    total_sum += cost

    again = input("Хочете ще щось? (так/ні): ").lower()
    if again != "так":
        break

print("\nВаше замовлення:")
for item in cart:
    print(f"- {item[0]} x{item[1]} = {item[2]} грн")

print(f"\nЗагальна сума до сплати: {total_sum} грн")
