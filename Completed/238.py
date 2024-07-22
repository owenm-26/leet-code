class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # explanation: iterate from left then from right, multiply nums[i] after 
        # adding the previous product to the answers array

        answer = [1] * len(nums) 
        product = 1

        # products from left
        for i in range(len(nums)):
            answer[i] = product
            product *= nums[i]
            
        # products from right and combine
        product = 1
        for i in range(len(nums)-1,-1 ,-1): 
            answer[i] *= product
            product *= nums[i]

        return answer