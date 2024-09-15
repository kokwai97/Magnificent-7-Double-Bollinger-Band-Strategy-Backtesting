def sell(entry, amount = None, share_unit = None, ticker = ticker):

    global balance
    global share
    
    time, column = entry
    
    price = column['Close']

    if share_unit is None: 
        share_unit = amount/price

    if share_unit >= 1.0:   # Minimum transaction size  
        balance += share_unit*price
        share -= share_unit  

    #print(f'{time}:  Sell {round(share_unit, 2)} {ticker} shares for ${round(price, 2)}.')