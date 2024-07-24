class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """

        # explanantion: if the string is len 1 then you cant fix. Otherwise find the 
        # first non 'a' and change it to an 'a'. Otherwise change the last letter to
        # 'b'

        if(len(palindrome) < 2):
            return ''
        middleIndex = (len(palindrome) / 2)  

        for i in range(middleIndex):
            if(palindrome[i] != 'a'):
                
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b'
       

