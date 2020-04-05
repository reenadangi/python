def maxProfit(prices):
    profit=0
    for i in range(1,len(prices)):
      profit += max(prices[i]-prices[i-1], 0) 
      
    return profit
print (maxProfit([7,3,2,5,6,4]))        

            
        
            


