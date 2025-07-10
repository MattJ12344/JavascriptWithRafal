class Solution(object):
    def binaryGap(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if(bin(n).count('1'))==1:
            return 0
        
        count:int = 0
        
        x:str = bin(n)[2:]
        
        for index in range(len(x)):
            
            if(x[index]=='1'):
                
                j=index+1
                while j<len(x):
                    
                    if(x[j]=='1'):
                        
                        count=max(j-index,count)
                        break
                    
                    j+=1
                    
        return count

sol = Solution()

# Test 1
assert sol.binaryGap(22) == 2

# Test 2
assert sol.binaryGap(8) == 0

# Test 3
assert sol.binaryGap(5) == 2

# Test 4
assert sol.binaryGap(6) == 1

# Test 5
assert sol.binaryGap(1) == 0

# Test 6
assert sol.binaryGap(9) == 3

# Test 7
assert sol.binaryGap(529) == 5

# Test 8
assert sol.binaryGap(0) == 0

print("nuda")