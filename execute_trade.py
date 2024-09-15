def execute_trade(position, signal, entry):
    
    time, column = entry
    
    if signal == +1:
        
        if position == 0:
            buy(entry, amount = balance)
        
        elif position == -1: # Close the short position first to establish a neutral position
            buy(entry, share_unit = -share)
            buy(entry, amount = balance)
        
    elif signal == -1: 
        
        if position == 0:
            sell(entry, amount = balance)
        
        elif position == +1: # Close the long position first to establish a neutral position
            sell(entry, share_unit = share)
            sell(entry, amount = balance)
    
    elif signal == 0:
        
        if position == +1:
            sell(entry, share_unit = share)
        
        elif position == -1:
            buy(entry, share_unit = -share)
    