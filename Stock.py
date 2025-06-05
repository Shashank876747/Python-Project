import requests
from bs4 import BeautifulSoup


def get_google_finance_price(ticker_symbol):
    url = f"https://www.google.com/finance/quote/{ticker_symbol}:NASDAQ"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(
            f"❌ Failed to retrieve data from Google Finance, status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    price_div = soup.find('div', class_='YMlKec fxKbKc')

    if price_div:
        return price_div.text
    else:
        print("❌ Could not find stock price on Google Finance.")
        return None


if __name__ == "__main__":
    symbol = input(
        "Enter stock ticker symbol (e.g., AAPL, MSFT, TSLA): ").strip().upper()
    price = get_google_finance_price(symbol)
    if price:
        print(f"🍏 {symbol} stock price on Google Finance: {price}")
