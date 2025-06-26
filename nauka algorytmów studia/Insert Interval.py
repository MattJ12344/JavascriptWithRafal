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

sol = Solution()

assert sol.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
assert sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
assert sol.insert([], [5,7]) == [[5,7]]
assert sol.insert([[1,5]], [2,3]) == [[1,5]]
assert sol.insert([[1,5]], [2,7]) == [[1,7]]
assert sol.insert([[1,5]], [6,8]) == [[1,5],[6,8]]
assert sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [17,20]) == [[1,2],[3,5],[6,7],[8,10],[12,16],[17,20]]
assert sol.insert([[1,5],[6,8]], [5,6]) == [[1,8]]

print("nuda")