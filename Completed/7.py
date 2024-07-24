class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # explanation: turn number into a list of strings so that reversal
        # is easier and join at the end and convert to signed int, checking
        # that is isnt beyond 32-bits

        reversedX = []
        sign = 1
        x = list(str(x))
        
        if(x[0] == '-'):
            sign = -1
            x = x[1:]
  
        for d in range(len(x)):
            reversedX.append(x.pop())

        answer =  int(''.join(reversedX)) 

        if(answer > 2**31 or answer < -2**31 -1):
            return 0
       
        
        return sign * answer
