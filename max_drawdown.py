def max_drawdown(data):
    running_max = data['Total_Returns'].cummax() 
    running_max[running_max < 1] = 1
    drawdown = (data['Total_Returns'])/running_max - 1
    max_dd = drawdown.min()*100
    #print(f'Maximum Drawdown: {round(max_drawdown, 2)}%')
    return round(max_dd, 2)