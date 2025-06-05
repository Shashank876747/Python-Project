import requests
from bs4 import BeautifulSoup


def get_apple_stock_price():
    url = "https://www.google.com/finance/quote/AAPL:NASDAQ"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve data, status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Inspect the page to find the tag containing the current price
    # Usually, the price is inside a <div> with data attributes or specific classes
    # This class is typical for the price on Google Finance
    price_div = soup.find('div', class_='YMlKec fxKbKc')
    if price_div:
        price = price_div.text
        return price
    else:
        print("Could not find stock price on the page.")
        return None


if __name__ == "__main__":
    price = get_apple_stock_price()
    if price:
        print(f"Apple (AAPL) stock price on Google Finance: {price}")
