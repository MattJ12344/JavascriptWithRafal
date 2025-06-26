
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        cloned: dict[str, int] = {}
        stack = [node]
        cloned[node] = Node(node.val)
        
        while stack:
            currentGraph = stack.pop()
            
            for neighbor in currentGraph.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                
                cloned[currentGraph].neighbors.append(cloned[neighbor])
        
        return cloned[node]
    
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]


sol = Solution()
cloned = sol.cloneGraph(n1)


assert cloned is not n1
assert cloned.val == 1
assert len(cloned.neighbors) == 2
neighbor_vals = sorted([n.val for n in cloned.neighbors])
assert neighbor_vals == [2, 4]


neighbor2 = [n for n in cloned.neighbors if n.val == 2][0]
assert sorted([n.val for n in neighbor2.neighbors]) == [1, 3]

neighbor3 = [n for n in neighbor2.neighbors if n.val == 3][0]
assert sorted([n.val for n in neighbor3.neighbors]) == [2, 4]

print("TESTY")