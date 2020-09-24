# You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

# paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

# Also, there is no garden that has more than 3 paths coming into or leaving it.

# Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

# Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.
# Example 1:

# Input: N = 3, paths = [[1,2],[2,3],[3,1]]
# Output: [1,2,3]
# Example 2:

# Input: N = 4, paths = [[1,2],[3,4]]
# Output: [1,2,1,2]

from collections import defaultdict

class Solution(object):
    def gardenNoAdj(self, N, paths):
        # create graph
        graph = defaultdict(list)
        for u,v in paths:
            graph[u].append(v)
            graph[v].append(u)
            
        colored = [0] * (N+1)

        def dfs(graph, node, colored):
            if colored[node] > 0:
                return True
            
            useless = set([colored[nxt] for nxt in graph[node] if colored[nxt] > 0])
            
            if len(useless) == 4:
                return False
            
            for color in [1,2,3,4]:
                if color in useless:
                    continue
                    
                colored[node] = color # colors is the available color for node
                
                isok = True
                # check if node with 'color' other nodes can be finished through dfs (point of dfs)
                for nxt in graph[node]:
                    if not dfs(graph, nxt, colored):
                        isok = False
                        break
                if isok:
                    return True
                
            return False
        
        for node in range(1, N + 1):
            dfs(graph, node, colored)

        return colored[1:]

sol=Solution()
print(sol.gardenNoAdj(4,[[1,2],[3,4]]))
