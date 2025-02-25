class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left, right = 0, len(s)-1
        while left < right and left < len(s) and right >= 0:

                # check if not the same and need to use skip
                if s[left] != s[right]:
                    tmp1 = s[:left] + s[left+1:]
                    tmp2 = s[:right] + s[right+1:]
                    return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
                else:
                    left+=1
                    right-=1
        return True