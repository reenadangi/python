def numOfIslands(grid):
    height=len(grid)
    if height==0: return 0
    width=len(grid[0])
    if width==0:
        return 0
    no_of_islands=0
    for i in range(height):
        for j in range(width):
            if grid[i][j]=='1':
                no_of_islands+=1
                dfs(grid,i,j)
    return no_of_islands
def dfs(grid,x,y):
    # make visted island - 2
    grid[x][y]='2'
    if x+1<len(grid) and grid[x+1][y]=='1':
        dfs(grid,x+1,y)
    if x-1>=0 and grid[x+1][y]=='1':
        dfs(grid,x-1,y)
    if y+1<len(grid[0]) and grid[x][y+1]=='1':
        dfs(grid,x,y+1)
    if y-1>=0 and grid[x][y-1]=='1':
        dfs(grid,x,y-1)
        
print(numOfIslands([["1","1","1","1","0"],["1","1","0","0","0"],["1","1","0","1","0"],["0","0","0","0","0"]]))




