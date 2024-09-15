def sortino_ratio(data, rf):
    negative_strat_returns = data[data['Strategy_Returns'] < 0]
    sortino_rat = (252**0.5)*(data['Strategy_Returns'].mean() - rf)/(negative_strat_returns['Strategy_Returns'].std())
    #print(f'Sortino Ratio: {round(sortino_ratio, 2)}')
    return round(sortino_rat, 2)