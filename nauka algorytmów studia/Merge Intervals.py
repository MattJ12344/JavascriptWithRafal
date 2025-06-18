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