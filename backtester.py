def backtester(position, share, rf, start_date, end_date, ticker):
    
    # Download the historical price data
    data = yf.download(ticker, start = start_date, end = end_date)

    # Compute the Double Bollinger Bands  
    data['SMA'] = data['Close'].rolling(20).mean()
    data['Std'] = data['Close'].rolling(20).std()

    data['A1'] = data['SMA'] + 2*data['Std']
    data['A2'] = data['SMA'] - 2*data['Std']

    data['B1'] = data['SMA'] + 1*data['Std']
    data['B2'] = data['SMA'] - 1*data['Std']

    data.drop(['Open', 'High', 'Low', 'Volume'], axis = 1, inplace = True, errors = 'ignore')
    data = data.dropna(axis = 0)

    # Generate the trading signals 
    data['Signal'] = np.where(data['Close'] > data['B1'], +1, 0)
    data['Signal'] = np.where(data['Close'] < data['B2'], -1, data['Signal'])

    # Calculate the daily returns based on the closing prices
    data['Returns'] = data['Close'].pct_change().fillna(0)

    # Calculate strategy returns
    data['Strategy_Returns'] = data['Returns'] * data['Signal'].shift(1).fillna(0)

    # Total number of trading days 
    total_trading_days = len(data)  

    # Iterate through each row of the stock dataframe
    for num, entry in enumerate(data.iterrows()):

        time, column = entry

        if num == data.shape[0] - 1: # Close all positions for the last trade
            signal = 0
        else:
            signal = column['Signal']

        execute_trade(position, signal, entry)

        position = signal # Update the latest position

    #print('\n')
    #print(f'Stock Ticker: {ticker}')
    #print(f'Final Capital Balance: ${round(balance, 2)}')
    
    # Compute the performance metrics 
    total_returns, annual_returns = returns(data, total_trading_days)
    annual_vol = annual_volatility(data)
    sharpe_rat = sharpe_ratio(data, rf)
    sortino_rat = sortino_ratio(data, rf)
    max_dd = max_drawdown(data) 

    return total_returns, annual_returns, annual_vol, sharpe_rat, sortino_rat, max_dd