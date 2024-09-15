# Magnificent 7 Tickers  
mag_7 = ['MSFT', 'AAPL', 'NVDA', 'AMZN', 'GOOG', 'META', 'TSLA']


# DF Columns 
total_return_list = []
annual_return_list = []
annual_volatility_list = [] 
sharpe_ratio_list = []
sortino_ratio_list = []
maximum_drawdown_list = []
final_cap_balance_list = []


# Loop through each stock ticker 
for ticker in mag_7:
    balance = 10000 # Initial capital balance
    position = 0 # Initial trading position
    share = 0 # Initial amount of shares owned
    rf = 0.01/252  # Assume an annual risk-free interest rate of 1%
    start_date = '2013-01-01'
    end_date = '2023-12-31'
    
    total_returns, annual_returns, annual_vol, sharpe_rat, sortino_rat, max_dd = backtester(position, share, rf, start_date, end_date, ticker = ticker)
    
    # Append values to columns
    final_cap_balance_list.append(round(balance, 2))
    total_return_list.append(total_returns)
    annual_return_list.append(annual_returns)
    annual_volatility_list.append(annual_vol) 
    sharpe_ratio_list.append(sharpe_rat)
    sortino_ratio_list.append(sortino_rat)
    maximum_drawdown_list.append(max_dd)
    

summary = {'Final Capital Balance ($)': final_cap_balance_list,
'Total Return (%)': total_return_list,
'Annual Return (%)': annual_return_list,
'Annual Volatility (%)': annual_volatility_list,
'Sharpe Ratio': sharpe_ratio_list,
'Sortino Ratio': sortino_ratio_list,
'Maximum Drawdown (%)': maximum_drawdown_list}

df = pd.DataFrame(summary, index = mag_7)