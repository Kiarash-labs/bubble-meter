# bubble-meter

**Data center spending passed $700B in 2026. Is this 1999 all over again?**

`bubble-meter` is a quantitative tool that compares the 2026 AI boom to the
dot-com bubble using historical price data. It measures four independent
bubble signals across both eras and lets the numbers speak for themselves.

## What it measures

For each stock in each era, the tool computes four metrics from daily price data:

- **Total return** — percentage growth from the first to the last trading day.
- **Annualized volatility** — how much the stock swings, scaled to a yearly figure (daily standard deviation × √252).
- **Max drawdown** — the largest peak-to-trough fall, in percent. The clearest signal of how brutally a bubble bursts.
- **Days to double** — how many trading days it took the price to first double from its starting value. A proxy for mania.

## Results

**AI boom (2022–2026)**

| Ticker | Total return % | Volatility % | Max drawdown % | Days to double |
|--------|---------------:|-------------:|---------------:|---------------:|
| NVDA   | 566.4 | 52.4 | -62.7 | 516 |
| MSFT   | 15.7  | 27.7 | -35.6 | —   |
| GOOGL  | 148.7 | 32.5 | -43.6 | 967 |
| AMZN   | 39.9  | 36.8 | -52.0 | —   |
| META   | 67.8  | 45.6 | -73.7 | 770 |
| ^GSPC  | 56.3  | 17.4 | -25.4 | —   |

**Dot-com (1995–2002)**

| Ticker | Total return % | Volatility % | Max drawdown % | Days to double |
|--------|---------------:|-------------:|---------------:|---------------:|
| CSCO   | 584.1  | 55.9 | -89.3 | 171 |
| INTC   | 302.4  | 51.0 | -82.2 | 117 |
| MSFT   | 601.1  | 40.5 | -65.2 | 360 |
| ORCL   | 416.7  | 63.1 | -84.2 | 374 |
| QCOM   | 1141.2 | 70.7 | -86.8 | 156 |
| ^GSPC  | 91.5   | 19.1 | -49.1 | 635 |
| ^IXIC  | 80.1   | 30.9 | -77.9 | 637 |

## Key finding

On these four signals, the dot-com era was substantially more extreme than the
2026 AI boom. Dot-com leaders fell 82–89% from peak (CSCO −89%, QCOM −87%),
while AI-era stocks fell 35–74%. Dot-com stocks also doubled far faster — some
in under 170 trading days — against 500–970 days in the AI era. By these
measures, 2026 does not yet resemble 1999 as closely as popular comparisons suggest.

## Limitations

This is an honest first pass, and the metrics have real blind spots:

- **No valuation data.** The tool measures price behavior, not fundamentals. Historical P/E ratios are not included (Cisco peaked near 200x in 2000; Nvidia around 50–75x in 2024–25), so it cannot judge whether prices were justified by earnings.
- **Survivorship bias.** The dot-com sample contains companies that *survived*. The ones that went to zero (Pets.com, Webvan, etc.) are not in the dataset, which makes that era look less severe than it actually was.
- **Small sample.** A handful of large-cap tickers per era, not the full market.

## How to run

```bash
python src/main.py
```

Requires `pandas` and `numpy`. Price data is included in `data/` (downloaded via
yfinance), so the analysis is fully reproducible without an internet connection.
