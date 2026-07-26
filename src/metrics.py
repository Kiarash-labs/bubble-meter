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


def bubble_score(volatility: float, drawdown: float, avg_days_to_double: float) -> float:
    """Combine volatility, drawdown and doubling speed into a 0-100 bubble score.

    Higher = more bubble-like. Total return is deliberately excluded, since high
    returns alone do not distinguish a bubble from genuine growth.
    """
    vol_score = volatility / 80
    drawdown_score = abs(drawdown) / 100
    speed_score = max(0, 1 - (avg_days_to_double / 1000))
    return round((vol_score + drawdown_score + speed_score) / 3 * 100, 1)
