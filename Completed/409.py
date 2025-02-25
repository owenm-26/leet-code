from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        unpaired = set()
        length = 0
        

        for i in range(len(s)):
            if s[i] in unpaired:
                unpaired.remove(s[i])
                length +=2
            else:
                unpaired.add(s[i])
        
        if len(unpaired) > 0:
            length +=1

        return length


        # # create a dictionary of letters to occurrences 
        # counts = Counter(s)

        # # sum all even counts 
        # evens_sum = sum([v for v in (counts.values()) if v % 2 == 0] + [0]) 

        # # then add 1 odd count and round the rest to even
        # odd_add = 0
        # odds_sum = 0
        # odds = [v for v in (counts.values()) if v % 2 == 1]
        # if len(odds) > 0:
        #     odds_sum = sum([(odd//2) * 2 for odd in odds]) 
        #     odd_add = 1

        # return evens_sum  + odds_sum + odd_add
        