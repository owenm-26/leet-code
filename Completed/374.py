# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

# explanation: binary search, maintain max and min and take average 

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [1, n]
        res = 2
        
        while res != 0 and n > 0:
            guessNum = (arr[0] + arr[1])//2
            res = guess(guessNum)
            if res == -1:
                arr[1] = guessNum-1
            else:
                arr[0] = guessNum+1
            

        return guessNum
        