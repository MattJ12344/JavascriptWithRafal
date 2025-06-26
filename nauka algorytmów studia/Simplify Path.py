from typing import List

class Solution(object):
    def simplifyPath(self, path: str) -> str:
        """
        :type path: str
        :rtype: str
        """
        path_stack: List[str] = []
        path_parts: List[str] = path.split("/")

        for part in path_parts:
            if part == "..":
                if path_stack:
                    path_stack.pop()
            elif part and part != ".":
                path_stack.append(part)

        return "/" + "/".join(path_stack)


sol = Solution()

assert sol.simplifyPath("/home/") == "/home"
assert sol.simplifyPath("/../") == "/"
assert sol.simplifyPath("/home//foo/") == "/home/foo"
assert sol.simplifyPath("/a/./b/../../c/") == "/c"
assert sol.simplifyPath("/a/../../b/../c//.//") == "/c"
assert sol.simplifyPath("/a//b////c/d//././/..") == "/a/b/c"

print("Przechodzi")