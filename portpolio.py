import quantstats as qs

qs.extend_pandas()

# stock = qs.utils.download_returns("GLD", period="10y")

# qs.reports.html(stock, title='PTL Investments', output='output/gld.html')

# qs.reports.html(stock, "SPY", title='GLD vs. SPY', output='output/gld_vs_spy.html')

# stock = qs.utils.download_returns("QQQ", period="10y")

# qs.reports.html(stock, "SPY", title='QQQ vs. SPY', output='output/qqq_vs_spy.html')

tickers = {
    "MSFT": 0.1,
    "AAPL": 0.4,
    "AMZN": 0.2,
    "GOOG": 0.3,
}
maag = portfolio = qs.utils.make_index(tickers)
qs.reports.html(maag, "qqq", title='MAAG vs. QQQ', output='output/maag_vs_qqq.html')