class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start=0
        best = 0

        # create current best
        for c in s[:k]:
            if(c in 'aeiou'):
                best = best + 1
        curCount=best
        
        # find better options in rest
        for i in range(k,len(s)):
            
            if(s[start] not in 'aeiou' and s[i] in 'aeiou'):
                curCount = curCount +1
                
            elif(s[start] in 'aeiou' and s[i] not in 'aeiou'):
                curCount = curCount - 1 
               
            if(curCount > best):
               
                best = curCount
            start = start + 1

        return best