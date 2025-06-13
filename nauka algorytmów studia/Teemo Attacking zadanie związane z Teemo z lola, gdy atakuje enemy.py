class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        n = len(timeSeries)

        for i in range(n-1):
            d= timeSeries[i+1] - timeSeries[i]
            res += duration if d > duration else d
        
        return res + (duration if n else 0)
