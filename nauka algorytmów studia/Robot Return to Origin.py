class Solution(object):
    def judgeCircle(self, moves: str) -> bool:
        """
        :type moves: str
        :rtype: bool
        """
        x:int = 0
        y:int = 0

        for move in moves:
            if move == 'U':
                y += 1

            elif move == 'D':
                y -= 1
             
            elif move == 'L':
                x -= 1
            
            elif move == 'R':
                x += 1  

        return x == y == 0
    
sol = Solution()

# Test 1
assert sol.judgeCircle("UD") == True

# Test 2
assert sol.judgeCircle("LL") == False

# Test 3
assert sol.judgeCircle("UDLR") == True

# Test 4
assert sol.judgeCircle("UUDDLLRR") == True

# Test 5
assert sol.judgeCircle("LLRRD") == False

# Test 6
assert sol.judgeCircle("") == True

# Test 7
assert sol.judgeCircle("UUU") == False

# Test 8
assert sol.judgeCircle("LDRRLRUULR") == False

print("Cos")