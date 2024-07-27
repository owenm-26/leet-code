class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # INEFFICIENT: explanation: same as Max Consecutive Ones III but k = 1 and you need
        # to account for the case where they are all ones as well as subtract one from the
        # end total because instead of flipping you delete
         
        zerosDeleted = 0
        best = 0
        start = 0

        for i in range(len(nums)):
            if(nums[i] == 0):
                zerosDeleted += 1
            while zerosDeleted > 1:
                if nums[start] == 0:
                    zerosDeleted -= 1
                start += 1
            best = max(best, i-start+1-1)

        if(zerosDeleted == 0):
            return len(nums) - 1
        else:
            return best