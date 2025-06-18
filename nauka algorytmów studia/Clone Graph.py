"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

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