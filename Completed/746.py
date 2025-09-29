class Solution:
    def minCostClimbingStairs(self, cost):
        M = [float("inf")] * len(cost)
        M[0] = cost[0]
        M[1] = cost[1]

        for i in range(2, len(M)):
            M[i] = cost[i] + min(M[i-1], M[i-2])
        
        return min(M[-1], M[-2])