def maxProfit(prices):
    l=0
    r=1
    max_profit=0
    n=len(prices)
    while r <n:
        if prices[l]< prices[r]:
            profit=prices[r]-prices[l]
            max_profit=max(max_profit,profit)
        else:
            l=r
        r+=1  

    return max_profit   
prices=[7,1,5,3,6,4]
      # update the buying point to prices[r] ,and moving to next day, 
result=maxProfit(prices)
print(result)
    
    