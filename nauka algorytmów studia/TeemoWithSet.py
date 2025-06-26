class Solution(object):
    def findPoisonedDuration(self, timeSeries: list[int], duration:int ) -> int :
        
        poisonedSeconds:set[int] = set()
        
        for momentAtaku in timeSeries:
            for sekundaZatrucia in range(momentAtaku, momentAtaku + duration):
                poisonedSeconds.add(sekundaZatrucia)

        return len(poisonedSeconds)



sol=Solution()

assert sol.findPoisonedDuration([1, 3, 5], 2) == 6

assert sol.findPoisonedDuration([1, 4], 2) == 4

assert sol.findPoisonedDuration([1, 2], 2) == 3

assert sol.findPoisonedDuration([], 2) == 0

assert sol.findPoisonedDuration([1,4,6,8,10,11], 2) == 11

assert sol.findPoisonedDuration([1, 3, 5], 0) == 0

assert sol.findPoisonedDuration([1, 3], 1000000) == 1000002

assert sol.findPoisonedDuration([1, 3, 5], 3) == 7

assert sol.findPoisonedDuration([1, 3, 5], 4) == 8

assert sol.findPoisonedDuration([1, 3, 5], 5) == 9

assert sol.findPoisonedDuration([1, 3, 5], 6) == 10

# set = [], input = timeseries= [1,3,5] duration= 2 
# output = 6

print("nuda")

