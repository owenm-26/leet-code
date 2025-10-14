class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        M = [0] * (amount+1)
        M[0] = 1
        
        for c in coins:
            for i in range(c, amount+1):
                M[i] += M[i-c] 
        # print(M)
        return M[amount]