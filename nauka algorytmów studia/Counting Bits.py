class Solution(object):
    def countBits(self, n:int)-> list[int]:
        """
        :type n: int
        :rtype: List[int]
        """
        bit_counts:list[int] = [0] * (n + 1)
        highestPowerOfTwo:int = 1

        for i in range(1, n + 1):
            if highestPowerOfTwo * 2 == i:
                highestPowerOfTwo = i
            
            bit_counts[i] = bit_counts[i - highestPowerOfTwo] + 1
        
        return bit_counts