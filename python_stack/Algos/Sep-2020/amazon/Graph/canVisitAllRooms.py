def canVisitAllRooms(rooms):
        n = len(rooms)
        visited = [False for _ in range(n)]

        def dfs(i):
            if visited[i]: return            
            visited[i] = True
            keys = rooms[i]
            for key in keys:
                dfs(key)
            return
        dfs(0)
        return all(visited)
print(canVisitAllRooms([[1],[2],[3],[]]))

def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False] * len(rooms)
        visited[0]=True
        stack=[0]
        while stack:
            node=stack.pop()
            for i in rooms[node]:
                if not visited[i]:
                    visited[i]=True
                    stack.append(i)
        return all(visited)
   