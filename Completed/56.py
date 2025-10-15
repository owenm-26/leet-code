class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        sol = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= sol[-1][1]:
                sol[-1][1] = max(end, sol[-1][1])
            else:
                sol.append([start, end])

        return sol

        