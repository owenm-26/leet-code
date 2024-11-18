class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n =len(s)
        longest = 0
        l=0
        r=0
        seen = {}

        while r < n:
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]]+1
            else:
                longest = max(longest, r-l+1)
            seen[s[r]] = r
            r+=1

        return longest


        

        