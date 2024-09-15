def sharpe_ratio(data, rf):
    sharpe_rat = (252**0.5)*(data['Strategy_Returns'].mean() - rf)/(data['Strategy_Returns'].std())
    #print(f'Sharpe Ratio: {round(sharpe_ratio, 2)}')
    return round(sharpe_rat, 2)