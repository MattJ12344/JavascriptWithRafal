class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                nul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

                p1, p2 = i + j, i + j + 1

                sum_ = nul + result[p2]

                result[p2] = sum_ % 10
                result[p1] += sum_ // 10
        result_str = ''.join(map(str, result))

        return result_str.lstrip('0')