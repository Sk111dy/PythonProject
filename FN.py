import requests
from bs4 import BeautifulSoup as bs


class MinfinParser:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        self.soup = None

    def auditSite(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = bs(response.text, "html.parser")
        else:
            raise ConnectionError("Не вдалося підключитися до сайту")

    def getInfo(self):
        Currency = []
        table = self.soup.find_all('tr', class_="sc-1x32wa2-4 dKDsVV")

        if not table:
            print("Не вдалося знайти таблицю валют")
            return Currency

        for i in table[1:6]:
            nameCurrency = i.find("a", class_="sc-1x32wa2-7 ciClTw")
            name = nameCurrency.text.strip() if nameCurrency else "?"

            price = i.find_all("td")

            def clean_number(text):
                text = text.replace(',', '.').strip()
                text = text.split()[0]
                result = ""
                dot_used = False

                for ch in text:
                    if ch.isdigit():
                        result += ch
                    elif ch == '.' and not dot_used:
                        result += ch
                        dot_used = True
                    else:
                        break

                return round(float(result), 2) if result else 0.0

            purchase = clean_number(price[1].text)
            sales = clean_number(price[2].text)

            Currency.append({
                "name": name,
                "buy": purchase,
                "sell": sales
            })

        return Currency

    def showInfo(self, currencies):
        print("\nКурси валют:\n")
        for i, c in enumerate(currencies, 1):
            print(f"{i}. {c['name']}: Купівля — {c['buy']} грн | Продаж — {c['sell']} грн")


url = "https://minfin.com.ua/ua/currency/"
parser = MinfinParser(url)

parser.auditSite()
currencies = parser.getInfo()

if not currencies:
    print("Дані не отримано")
    exit()

parser.showInfo(currencies)

print("\n1 - Купити\n2 - Продати")
action = int(input("> "))

print("\nВиберіть валюту:")
currency_index = int(input("> ")) - 1

print("\nСума в гривнях:")
uah = float(input("> "))

currency = currencies[currency_index]

if action == 1:
    result = uah / currency["sell"]
    print(f"\nВи купите {result:.2f} {currency['name']}")

elif action == 2:
    result = uah / currency["buy"]
    print(f"\nВи продасте {result:.2f} {currency['name']}")

else:
    print("Невірний вибір")