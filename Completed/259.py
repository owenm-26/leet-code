class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        # explanation: rule is that anything mod 9 (unless remainder is 0) is the 
        # answer, otherwise answer 9

        if num == 0:
            return 0
        else:
            return num%9 if num%9 !=0 else 9


        # print('num', num)
        # digits = len(str(num))

        # if digits == 1:
        #     return num
        
        # curSum = 0
        # for d in str(num):
        #     curSum += int(d)
        
        # return self.addDigits(curSum)