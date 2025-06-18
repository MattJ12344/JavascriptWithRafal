class Solution(object):
    def isInterleave(self, first: str, second: str, trird: str) -> bool:
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        firstLength: int= len(first), 
        secondLength: int= len(second)

        if firstLength + secondLength != len(trird):
            return False

        dynamicProgramming: list[bool] = [False] * (secondLength + 1)
        dynamicProgramming[0] = True

        for j in range(1, secondLength + 1):
            dynamicProgramming[j] = dynamicProgramming[j - 1] and second[j - 1] == trird[j - 1]


        for i in range(1, firstLength + 1):
            dynamicProgramming[0] = dynamicProgramming[0] and first[i - 1] == trird[i - 1]
            
            for j in range(1, secondLength + 1):
                dynamicProgramming[j] = (dynamicProgramming[j] and first[i - 1] == trird[i + j - 1]) or \
                        (dynamicProgramming[j - 1] and second[j - 1] == trird[i + j - 1])
                        

        return dynamicProgramming[secondLength]