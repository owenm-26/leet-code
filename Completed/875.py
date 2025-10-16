import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)

        k = maxPile
        rightBound = maxPile
        leftBound = 1

        seen = {}

        def solutionWorks(val):
            """O(n) that returns if it works and the remainder"""
            if val in seen:
                return seen[val]
            hours = 0
            for p in piles:
                hours += math.ceil(p / val)
            seen[val] = (hours <= h, h-hours)
            return (hours <= h, h-hours)

        def binarySearchHelper(val, rightBound, leftBound, best_k):
            """Finds k via binary search"""

            if rightBound == leftBound:
                return best_k
            
            print(f"Running for {val}. [{leftBound}, {rightBound}]")
            (works, rem) = solutionWorks(val)

            if works:
                if val < best_k:
                    best_k = val
                    rightBound = val

            else:
                leftBound = val+1
            
            nextTry = leftBound + (rightBound-leftBound)//2
            return binarySearchHelper(nextTry, rightBound, leftBound, best_k)

        first = leftBound + (rightBound-leftBound)//2
        return binarySearchHelper(first, rightBound, leftBound, k)
