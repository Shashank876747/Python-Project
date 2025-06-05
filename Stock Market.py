import yfinance as yf


def get_stock_info(ticker_symbol):
    try:
        stock = yf.Ticker(ticker_symbol)
        stock_info = stock.info

        print(f"🔎 Stock: {stock_info['longName']} ({ticker_symbol.upper()})")
        print(f"📅 Market: {stock_info.get('exchange', 'N/A')}")
        print(f"💵 Current Price: ${stock_info['currentPrice']}")
        print(f"📈 Day High: ${stock_info['dayHigh']}")
        print(f"📉 Day Low: ${stock_info['dayLow']}")
        print(f"🪙 Market Cap: ${stock_info['marketCap']}")
        print(f"📊 P/E Ratio: {stock_info.get('trailingPE', 'N/A')}")
        print(
            f"📍 52-Week Range: ${stock_info.get('fiftyTwoWeekLow', 'N/A')} - ${stock_info.get('fiftyTwoWeekHigh', 'N/A')}")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    symbol = input(
        "Enter stock ticker symbol (e.g., AAPL, MSFT, TSLA): ").strip()
    get_stock_info(symbol)
