class Solution(object):
    def multiply(self, first: str, second: str) -> str:
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if first == "0" or second == "0":
            return "0"
        
        firstLength: int = len(first)
        secondLength: int = len(second)
        result: list[int] = [0] * (firstLength + secondLength)

        for i in range(firstLength - 1, -1, -1):
            
            for j in range(secondLength - 1, -1, -1):
                multiply = (ord(first[i]) - ord('0')) * (ord(second[j]) - ord('0'))

                position1: int = i + j
                position2: int = i + j + 1

                currnetSum: int = multiply + result[position2]

                result[position2] = currnetSum % 10
                result[position1] += currnetSum // 10

                
        resultStr: str = ''.join(map(str, result))

        return resultStr.lstrip('0')
    
sol = Solution()

assert sol.multiply("2", "3") == "6"
assert sol.multiply("123", "456") == "56088"
assert sol.multiply("0", "12345") == "0"
assert sol.multiply("999", "999") == "998001"
print("OK")