from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count:int = 0
        length:int  = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                empty_left:bool = (i == 0 or flowerbed[i - 1] == 0)
                empty_right:bool = (i == length - 1 or flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n


sol = Solution()

assert sol.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True

assert sol.canPlaceFlowers([1, 0, 0, 0, 1], 2) == False

assert sol.canPlaceFlowers([0, 0, 0, 0, 0], 3) == True

assert sol.canPlaceFlowers([0], 1) == True

assert sol.canPlaceFlowers([1], 0) == True

assert sol.canPlaceFlowers([1], 1) == False

assert sol.canPlaceFlowers([0, 0, 1, 0, 0], 2) == True

print("Nuda")