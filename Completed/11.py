class Solution:
    def maxArea(self, heights):
        curr_max = 0

        l,r = 0, len(heights)-1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            curr_max = max(curr_max, area)

            if(heights[l] < heights[r]):
                l+=1
            else:
                r-=1

        return curr_max
        