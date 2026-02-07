from dataclasses import dataclass
from typing import Dict


@dataclass
class StockPosition:
    symbol: str
    shares: float
    buy_price: float

    def invested_amount(self) -> float:
        return self.shares * self.buy_price


class StockPortfolio:
    def __init__(self, name: str = "My Portfolio"):
        self.name = name
        self.positions: Dict[str, StockPosition] = {}

    def add_stock(self, symbol: str, shares: float, buy_price: float) -> None:
        symbol = symbol.upper().strip()
        if shares <= 0 or buy_price <= 0:
            raise ValueError("Shares and buy price must be greater than 0.")

        if symbol in self.positions:
            current = self.positions[symbol]
            total_shares = current.shares + shares
            weighted_price = (
                (current.shares * current.buy_price) + (shares * buy_price)
            ) / total_shares
            self.positions[symbol] = StockPosition(symbol, total_shares, weighted_price)
        else:
            self.positions[symbol] = StockPosition(symbol, shares, buy_price)

    def remove_stock(self, symbol: str) -> None:
        self.positions.pop(symbol.upper().strip(), None)

    def invested_total(self) -> float:
        return sum(p.invested_amount() for p in self.positions.values())

    def current_total(self, market_prices: Dict[str, float]) -> float:
        total = 0.0
        for symbol, position in self.positions.items():
            current_price = market_prices.get(symbol, position.buy_price)
            total += current_price * position.shares
        return total

    def summary(self, market_prices: Dict[str, float]) -> str:
        lines = []
        lines.append(f"Portfolio: {self.name}")
        lines.append("-" * 72)
        lines.append(
            f"{'Symbol':<10}{'Shares':>10}{'Buy':>12}{'Current':>12}{'P/L':>14}"
        )
        lines.append("-" * 72)

        invested = self.invested_total()
        current = self.current_total(market_prices)

        for symbol, position in sorted(self.positions.items()):
            curr_price = market_prices.get(symbol, position.buy_price)
            pl = (curr_price - position.buy_price) * position.shares
            lines.append(
                f"{symbol:<10}{position.shares:>10.2f}{position.buy_price:>12.2f}{curr_price:>12.2f}{pl:>14.2f}"
            )

        net = current - invested
        pct = (net / invested * 100) if invested else 0.0
        lines.append("-" * 72)
        lines.append(f"{'Invested':<20}: ${invested:,.2f}")
        lines.append(f"{'Current Value':<20}: ${current:,.2f}")
        lines.append(f"{'Net P/L':<20}: ${net:,.2f} ({pct:.2f}%)")
        return "\n".join(lines)


def demo() -> None:
    portfolio = StockPortfolio("Sample Tech Portfolio")

    portfolio.add_stock("AAPL", 10, 180)
    portfolio.add_stock("MSFT", 5, 420)
    portfolio.add_stock("NVDA", 8, 110)
    portfolio.add_stock("AAPL", 2, 190)

    market_prices = {
        "AAPL": 195,
        "MSFT": 430,
        "NVDA": 125,
    }

    print(portfolio.summary(market_prices))


if __name__ == "__main__":
    demo()
