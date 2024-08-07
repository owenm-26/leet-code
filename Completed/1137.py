class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # explanation: just shifting down the view essentially, dont need a table

        a,b,c = 0, 1, 1

        if n <= 2:
            return 0 if n==0 else 1

        for i in range(2, n):
            a,b,c = b, c, c + a + b
        return c

        # M = [0,1,1]

        # if( n <= 2):
        #     return M[n]

        # for i in range(3,n+1):
        #     M.append(M[i-3] + M[i-2] + M[i-1]) 
        # return M[n]
            
        