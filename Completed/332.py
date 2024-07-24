class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
    # explanation: greedy won't work since the best option isnt always biggest first
    # dp allows us to build up to the solution. Outerloop is values between 1 and 
    # the amount we need and the inner loop calculates the cheapest way to get 
    # there

        dp = [0] + [float('inf')] * amount

        for i in range (1, amount+1):
            for coin in coins:
                if(coin <= i):
                    dp[i] = min(dp[i], dp[i-coin]+1)
        if(dp[-1] == float('inf')):
            return -1
        return dp[-1]




           


        