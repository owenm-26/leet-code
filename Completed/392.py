class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) == 0):
            return True
        if( len(s) > len(t)):
            return False
        # change s each time 
        for i in range(len(t)):
            if(t[i] == s[0]):
                s=s[1:]
            if(len(s) == 0):
                return True
        return False

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) == 0):
            return True
        if(len(s) > len(t)):
            return False
        checkIndex = 0
        for i in range(len(t)):
            # change pointer each time
            if(t[i] == s[checkIndex]):
                checkIndex +=1
            if(checkIndex == len(s)):
                return True
        return False
            