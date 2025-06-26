class Solution(object):
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n:int) -> int:
        
        result:int = 0
        
        for i in range(32):
            result = (result << 1) 
            result += (n & 1)
            n = n >>1
            
        return result
    
sol = Solution()

# Test 1
assert sol.reverseBits(43261596) == 964176192

# Test 2
assert sol.reverseBits(0xFFFFFFFF) == 0xFFFFFFFF

# Test 3
assert sol.reverseBits(0) == 0

# Test 4
assert sol.reverseBits(1) == 0x80000000

# Test 5
assert sol.reverseBits(2) == 0x40000000

print("Byc")