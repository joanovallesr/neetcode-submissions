"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def clone(self, node, visited):
        if node in visited:
            return visited[node]
        
        clonedNode = Node(node.val)
        visited[node] = clonedNode
        for neighbor in node.neighbors:
            clonedNode.neighbors.append(self.clone(neighbor, visited))

        return clonedNode

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        visited = {}
        return self.clone(node, visited)