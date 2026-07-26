import pandas as pd


class Era:
    def __init__(self, name, start, end, tickers, folder):
        self.name = name
        self.start = start
        self.end = end
        self.tickers = tickers
        self.folder = folder

    def load_data(self):
        self.data = {}
        for ticker in self.tickers:
            df = pd.read_csv(
                f"{self.folder}/{ticker}.csv",
                skiprows=[1, 2],
                index_col=0,
                parse_dates=True,
            )
            self.data[ticker] = df

    def get_prices(self, ticker):
        return self.data[ticker]["Close"]
