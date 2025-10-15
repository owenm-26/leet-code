class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        b = [float("-inf")] * n
        s = [0] * n
        
        # this only works bc of python reverse indexing and bc s[-1] and s[-2] are init to 0
        for i in range(n): 
            s[i] = max(s[i-1], prices[i] + b[i-1]) # max of (sell prev with cooldown, sell cur given you bought it just before)
            b[i] = max(b[i-1], s[i-2] - prices[i]) # max of (already bought prev, sold 2 turns ago [cooldown] and are now buying again)
        
        return s[n-1]
        
      
       
            
