class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = []
        #get rid of non alpha / nums
        for i in range(len(s)):
            if s[i].isalnum():
                string.append(s[i].lower())
       
       # two pointer solution
        p1 = 0
        p2 = len(string)-1

        while p1 <= p2:
            if string[p1] != string[p2]:
                return False
            p1 += 1
            p2 -= 1

        return True
