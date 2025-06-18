class Solution(object):
    def insert(self, intervals:list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()

        result: list[list[int]] = [intervals[0]]

        for i in range(1, len(intervals)):
            
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
                
            else:
                result.append(intervals[i])


        return result
        