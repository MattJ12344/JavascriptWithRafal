class Solution(object):
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        mergedIntervals: list[list[int]] = []
        intervals.sort(key=lambda x: x[0])

        previousIntervals: list[int] = intervals[0]

        for interval in intervals[1:]:
            
            if interval[0] <= previousIntervals[1]:
                previousIntervals[1] = max(previousIntervals[1], interval[1])
                
            else:
                mergedIntervals.append(previousIntervals)
                previousIntervals = interval
                
        
        mergedIntervals.append(previousIntervals)


        return mergedIntervals
    
sol = Solution()


assert sol.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]

assert sol.merge([[1,4]]) == [[1,4]]

assert sol.merge([[1,4],[2,3]]) == [[1,4]]

assert sol.merge([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]]

assert sol.merge([[1,4],[0,2],[3,5]]) == [[0,5]]

print("KOD")