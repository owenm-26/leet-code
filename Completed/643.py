class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        # explanation: find the first window's avg then slide over, subtracting
        # the removed elements avg and adding the new elements avg and comparing
        # to current best
       
        if(k >= len(nums)):
            return float(sum(nums))/k
        if(k == 1):
            return max(nums)

        best = 0.0
        start = 0
        end = k
        
        for i in range(k):
            best += float(nums[i]) / k
        
        newAvg = best
        while end < len(nums):
            newAvg = newAvg - float(nums[start])/k + float(nums[end])/k
            best = max(best, newAvg)
            start+=1
            end +=1
       
        return best 

        