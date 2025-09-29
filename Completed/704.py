class Solution:
    def search(self, nums, target):

        def search_helper( nums, target, offset):
            if (len(nums) == 1 and nums[0] != target):
                return -1
            
            index = len(nums) // 2

            if(nums[index] > target):
                return search_helper(nums[:index], target, offset)

            if(nums[index] < target):
                return search_helper(nums[index:], target, (offset+index))

            if(nums[index] == target):
                return offset + index

        return search_helper(nums, target, 0)