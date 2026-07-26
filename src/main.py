import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pandas as pd

from era import Era
from metrics import total_return, annualized_volatility, max_drawdown, days_to_double


def analyze_era(era: Era) -> pd.DataFrame:
    """Run all metrics on each ticker in an era and return a table."""
    era.load_data()
    rows = []
    for ticker in era.tickers:
        prices = era.get_prices(ticker)
        rows.append({
            "ticker": ticker,
            "total_return_%": round(total_return(prices), 1),
            "volatility_%": round(annualized_volatility(prices), 1),
            "max_drawdown_%": round(max_drawdown(prices), 1),
            "days_to_double": days_to_double(prices),
        })
    return pd.DataFrame(rows)


def main() -> None:
    ai = Era(
        "AI-boom", "2022-01-01", "2026-07-01",
        ["NVDA", "MSFT", "GOOGL", "AMZN", "META", "^GSPC"],
        "data/ai",
    )
    dotcom = Era(
        "Dot-com", "1995-01-01", "2002-12-31",
        ["CSCO", "INTC", "MSFT", "ORCL", "QCOM", "^GSPC", "^IXIC"],
        "data/dotcom",
    )

    print("=== AI boom (2022-2026) ===")
    print(analyze_era(ai).to_string(index=False))
    print()
    print("=== Dot-com (1995-2002) ===")
    print(analyze_era(dotcom).to_string(index=False))


if __name__ == "__main__":
    main()
