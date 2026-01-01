import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("article.product_pod")[:8]

results = []

for book in books:
    # Назва книги
    title = book.h3.a["title"]

    # Ціна
    price = book.select_one("p.price_color").text.strip()

    # Рейтинг у вигляді слова (One, Two, Three...)
    rating_class = book.select_one("p.star-rating")["class"]
    # Другий клас — це рейтинг
    rating = [c for c in rating_class if c != "star-rating"][0]

    results.append({
        "title": title,
        "price": price,
        "rating": rating
    })

# Виводимо результат
for i, book in enumerate(results, start=1):
    print(f"{i}. {book['title']} — {book['price']} — Rating: {book['rating']}")
