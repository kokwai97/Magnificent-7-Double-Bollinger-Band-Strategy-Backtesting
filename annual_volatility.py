def annual_volatility(data):
    annual_vol = (data['Strategy_Returns'].std())*(252**0.5)*100
    #print(f'Annual Volatility: {round(annual_volatility, 2)}%')
    return round(annual_vol, 2)