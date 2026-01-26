import yfinance as yf
class Stock:
    """Represents a single stock holding."""
    def __init__(self, symbol, quantity, purchase_price, company_name=""):
        self.symbol = symbol
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.company_name = company_name
    
    def current_value(self, current_price):
        """Calculate current value of the stock."""
        return self.quantity * current_price
    
    def gain_loss(self, current_price):
        """Calculate gain or loss."""
        return (current_price - self.purchase_price) * self.quantity
    
    def gain_loss_percent(self, current_price):
        """Calculate gain or loss percentage."""
        if self.purchase_price == 0:
            return 0
        return ((current_price - self.purchase_price) / self.purchase_price) * 100


class Portfolio:
    """Represents a collection of stock holdings."""
    def __init__(self, name="My Portfolio"):
        self.name = name
        self.stocks = {}
    
    def add_stock(self, symbol, quantity, purchase_price, company_name=""):
        """Add or update a stock in the portfolio."""
        if symbol in self.stocks:
            print(f"Updating {symbol}...")
        self.stocks[symbol] = Stock(symbol, quantity, purchase_price, company_name)
        print(f"Added/Updated {quantity} shares of {symbol} ({company_name}) at ${purchase_price}")
    
    def remove_stock(self, symbol):
        """Remove a stock from the portfolio."""
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"Removed {symbol} from portfolio")
        else:
            print(f"{symbol} not found in portfolio")
    
    def update_price(self, symbol, current_price):
        """Update the current price of a stock."""
        if symbol in self.stocks:
            return self.stocks[symbol].current_value(current_price)
        else:
            print(f"{symbol} not found in portfolio")
            return 0
    
    def get_portfolio_summary(self, prices=None):
        """
        Display portfolio summary.
        prices: dict with symbol as key and current_price as value
                If None, fetches live prices from yfinance
        """
        # Fetch live prices if not provided
        if prices is None:
            print("Fetching live stock prices...")
            prices = {}
            for symbol in self.stocks.keys():
                try:
                    ticker = yf.Ticker(symbol)
                    price = ticker.info.get('currentPrice') or ticker.info.get('regularMarketPrice')
                    if price:
                        prices[symbol] = float(price)
                    else:
                        prices[symbol] = self.stocks[symbol].purchase_price
                except Exception as e:
                    print(f"Warning: Could not fetch price for {symbol}: {e}")
                    prices[symbol] = self.stocks[symbol].purchase_price
        
        print(f"\n{'='*125}")
        print(f"Portfolio: {self.name}")
        print(f"{'='*125}")
        print(f"{'Company':<30}{'Symbol':<8}{'Qty':<10}{'Buy Price':<14}{'Current Price':<16}{'Change':<14}{'Change %':<12}{'Value':<14}")
        print(f"{'-'*125}")
        
        total_invested = 0
        total_current_value = 0
        
        for symbol, stock in self.stocks.items():
            current_price = prices.get(symbol, stock.purchase_price)
            current_value = stock.current_value(current_price)
            gain_loss = stock.gain_loss(current_price)
            gain_loss_pct = stock.gain_loss_percent(current_price)
            price_change = current_price - stock.purchase_price
            
            invested = stock.purchase_price * stock.quantity
            total_invested += invested
            total_current_value += current_value
            
            change_str = f"${price_change:+.2f}"
            print(f"{stock.company_name:<30}{symbol:<8}{stock.quantity:<10.6f}${stock.purchase_price:<13.2f}${current_price:<15.2f}{change_str:<14}{gain_loss_pct:>10.2f}%${current_value:<13.2f}")
        
        print(f"{'-'*125}")
        total_gain_loss = total_current_value - total_invested
        total_return = (total_gain_loss / total_invested * 100) if total_invested > 0 else 0
        
        print(f"{'':30}{'TOTAL':<8}{'':10}${total_invested:<13.2f}${total_current_value:<15.2f}${total_gain_loss:+.2f}          {total_return:>10.2f}%${total_current_value:<13.2f}")
        print(f"{'='*125}\n")
        
        return {
            'total_invested': total_invested,
            'total_current_value': total_current_value,
            'total_gain_loss': total_gain_loss,
            'total_return_percent': total_return
        }


def main():
    # Create a portfolio
    portfolio = Portfolio("My Tech Stock Portfolio")
    
    # Add stocks - Investment Date: 11/28/2025
    # Green stocks ($20 each)
    portfolio.add_stock("NVDA", 0.111794, 20.00, "NVIDIA")
    portfolio.add_stock("TSM", 0.068336, 20.00, "Taiwan Semiconductor")
    portfolio.add_stock("MSFT", 0.041044, 20.00, "Microsoft")
    portfolio.add_stock("AAPL", 0.072112, 20.00, "Apple")
    
    # Yellow stocks ($10 each)
    portfolio.add_stock("AMD", 0.04624, 10.00, "Advanced Micro Devices Inc.")
    portfolio.add_stock("INTC", 0.267522, 10.00, "Intel")
    portfolio.add_stock("ASML", 0.009618, 10.00, "ASML Holding NV")
    portfolio.add_stock("AVGO", 0.025035, 10.00, "Broadcom")
    portfolio.add_stock("QCOM", 0.060595, 10.00, "Qualcomm")
    portfolio.add_stock("MU", 0.042489, 10.00, "Micron")
    portfolio.add_stock("TXN", 0.060226, 10.00, "Texas Instruments")
    portfolio.add_stock("LRCX", 0.064259, 10.00, "Lam Research")
    portfolio.add_stock("NOK", 1.64609, 10.00, "Nokia")
    portfolio.add_stock("GOOG", 0.030954, 10.00, "Alphabet")
    portfolio.add_stock("DELL", 0.074532, 10.00, "Dell Technologies")
    
    # Fetch and display portfolio summary with live prices
    portfolio.get_portfolio_summary()


if __name__ == "__main__":
    main()
