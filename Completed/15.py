class Solution:
    def threeSum(self, nums):
        ans = []
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            # skip the "a" position for duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i+1, n-1
            while l < r:
                summed = nums[i] + nums[l] + nums[r]

                if summed == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

                if summed > 0: 
                    r -=1
                
                if summed < 0:
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        return ans

