from typing import List

class Solution(object):
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        :type s: str
        :rtype: List[str]
        """
        validIp: List[str] = []
        self.dfs(s, 0, "", validIp)
        return validIp

    def dfs(self, remaining: str, partIndex: int, currentIp: str, validIp: List[str]) -> None:
        if partIndex > 4:
            return

        if partIndex == 4 and not remaining:
            validIp.append(currentIp[:-1])  # remove last dot
            return

        for i in range(1, len(remaining) + 1):
            segment = remaining[:i]
            if segment == "0" or (segment[0] != "0" and 0 < int(segment) < 256):
                self.dfs(remaining[i:], partIndex + 1, currentIp + segment + ".", validIp)
                

sol = Solution()

# Test 1
result1 = sorted(sol.restoreIpAddresses("25525511135"))
assert result1 == sorted(["255.255.11.135", "255.255.111.35"])

# Test 2
result2 = sol.restoreIpAddresses("0000")
assert result2 == ["0.0.0.0"]

# Test 3
result3 = sorted(sol.restoreIpAddresses("101023"))
expected3 = sorted([
    "1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"
])
assert result3 == expected3

# Test 4
result4 = sol.restoreIpAddresses("1111")
assert result4 == ["1.1.1.1"]

# Test 5
result5 = sol.restoreIpAddresses("123")
assert result5 == []  

print("OKEJ")