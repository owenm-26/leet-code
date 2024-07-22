class Solution(object):
    def increasingTriplet(nums: []):
        length =len(nums)
        if(length < 3):
            return False
        
        for i in range(length -2):
            if(nums[i] < nums[i+1] and nums[i+1] < nums[i+2]):
                return True
        return False 
    
    answer = increasingTriplet([2,1,5,0,4,6])
    print(answer)