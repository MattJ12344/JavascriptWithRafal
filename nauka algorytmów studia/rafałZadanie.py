class Solution(object):
    def findPoisonedDuration(self, timeSeries: list[int], duration:int ) -> int :
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        # Input: timeSeries = [1,4], duration = 2
        # 1s duration: 1,2
        # 4s duration: 4, 5
        # poison duration sum = 4
        
        # timeSeries = [1,2], duration = 2
        # 1s duration: 1, 2
        # 2s duration: 2, 3
        # poison duration sum = 3
        
        result:int = 0
        
        number:int = len(timeSeries)
        
        for index in range(number - 1):
            
            timer:int = timeSeries[index + 1] - timeSeries[index]
            
            if timer > duration:
                result += duration
                
            else:
                result += timer
        
        if number > 0:
            result += duration
        
        return result
        
        
sol=Solution()

print("nuda")
        

assert sol.findPoisonedDuration([1, 3, 5], 2) == 6

assert sol.findPoisonedDuration([1, 4], 2) == 4

assert sol.findPoisonedDuration([1, 2], 2) == 3

assert 2==2
# assert 2==3

print("telefon")

