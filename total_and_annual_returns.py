def returns(data, total_trading_days):
    data['Total_Returns'] = (data['Strategy_Returns'] + 1).cumprod()
    total_returns = data.iloc[-1]['Total_Returns']*100
    annual_returns = (data.iloc[-1]['Total_Returns']**(252/total_trading_days) - 1)*100
        
    #print(f'Total Returns: {round(total_returns, 2)}%')
    #print(f'Annual Returns: {round(annual_returns, 2)}%')
    return round(total_returns, 2), round(annual_returns, 2)