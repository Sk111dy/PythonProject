import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("article.product_pod")[:8]

results = []

for book in books:
    title = book.h3.a["title"]

    price = book.select_one("p.price_color").text.strip()


    rating_class = book.select_one("p.star-rating")["class"]

    rating = [c for c in rating_class if c != "star-rating"][0]

    results.append({
        "title": title,
        "price": price,
        "rating": rating
    })


for i, book in enumerate(results, start=1):
    print(f"{i}. {book['title']} — {book['price']} — Rating: {book['rating']}")
