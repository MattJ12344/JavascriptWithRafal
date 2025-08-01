class Solution(object):
    def countAndSay(self, n:int) -> str:
        result="1"
        
        for _ in range(n-1):
            
            count: int =0
            CurrentString: str=result[0]
            nextTerm: str=""
            
            for j in range(len(result)):
                
                if result[j]==CurrentString:
                    count=count+1
                    
                    if j==len(result)-1:
                        nextTerm=nextTerm+str(count)+CurrentString

                else:
                    nextTerm=nextTerm+str(count)+CurrentString
                    count=1
                    CurrentString=result[j]
                    
                    if j==len(result)-1:
                        nextTerm=nextTerm+str(count)+CurrentString
            
            result=nextTerm
            
        return result

sol = Solution()

assert sol.countAndSay(1) == "1"
assert sol.countAndSay(2) == "11"
assert sol.countAndSay(3) == "21"
assert sol.countAndSay(4) == "1211"
assert sol.countAndSay(5) == "111221"
assert sol.countAndSay(6) == "312211"
assert sol.countAndSay(7) == "13112221"

print("Nuda")
