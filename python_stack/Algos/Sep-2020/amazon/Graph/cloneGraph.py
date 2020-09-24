class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
def cloneGraph(self, node):
        def helper(node, seen):
            if node in seen:
                return seen[node]

            copy = Node(node.val, [])
            seen[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(helper(neighbor, seen))       
            return copy   

        if not node:
            return node
        return helper(node, {})