class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        # explanation: there is only a collision when a left moving asteroid
        # is added to a stack with right moving asteroids. Thus default to adding
        # to stack unless case met. If case met, go down stack until asteroid is 
        # destroyed/is at end
        
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        
        return stack