import quantstats as qs

qs.extend_pandas()

stock_google = qs.utils.download_returns("GOOG")
print(stock_google)

# sharpe_ratio = qs.stats.sharpe(stock_google)
# print(stock_google.cagr())
#
# print(stock_google.monthly_returns())
# print(stock_google.max_drawdown())

# qs.plots.earnings()
stock_google.plot_earnings(savefig="output/goog_earnings.png", start_balance=100_000)
stock_google.plot_monthly_heatmap(savefig="output/goog_monthly_heatmap.png")