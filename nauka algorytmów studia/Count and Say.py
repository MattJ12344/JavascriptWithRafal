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