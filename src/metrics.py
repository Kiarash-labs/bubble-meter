import numpy as np
import pandas as pd


def total_return(prices: pd.Series) -> float:
    """Percentage growth from the first to the last price."""
    first = prices.iloc[0]
    last = prices.iloc[-1]
    return (last / first - 1) * 100


def annualized_volatility(prices: pd.Series) -> float:
    """Annualized volatility: std of daily returns scaled by sqrt(252)."""
    daily_returns = prices.pct_change().dropna()
    return daily_returns.std() * np.sqrt(252) * 100


def max_drawdown(prices: pd.Series) -> float:
    """Largest peak-to-trough decline, in percent."""
    running_max = prices.cummax()
    drawdown = (prices - running_max) / running_max
    return drawdown.min() * 100


def days_to_double(prices: pd.Series):
    """Number of trading days until the price first doubles from its start value."""
    start = prices.iloc[0]
    target = start * 2
    for i in range(len(prices)):
        if prices.iloc[i] >= target:
            return i
    return None
