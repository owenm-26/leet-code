class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # explanation: we only care about the lowest sell price and profit.
        # iterate through linearly and update them both
        if(len(prices) == 0):
            return 0
        
        lowestBuy = prices[0]
        profit = 0
        
        for i in range(1,len(prices)):
            if(prices[i] - lowestBuy > profit):
                profit = prices[i] - lowestBuy
            if(prices[i] < lowestBuy):
                lowestBuy = prices[i]

        return profit
