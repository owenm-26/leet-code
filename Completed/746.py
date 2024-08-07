class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        # explanation: DP solution and check the top of the stairs [-1] for the best solution
        M = {}
        M[0] = 0
        M[1] = cost[0]
        cost.append(0)

        for i in range(2,len(cost)+1):
            M[i] =min(M[i-2] + cost[i-1], M[i-1] + cost[i-1])

        return M[M.keys()[-1]]


        # n = len(cost)

        # if n == 0:
        #     return 0
        # elif n < 3:
        #     return min(cost[0], cost[1])
        # else:
        #     M = [0] * n
        #     M[0] = cost[0]
        #     M[1] = cost[1]
        #     for i in range(2, n):
        #         M[i] = cost[i] + min(M[i-1], M[i-2])
        #     return min(M[-1], M[-2])

        