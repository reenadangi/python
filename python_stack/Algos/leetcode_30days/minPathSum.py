def minPathSum(grid):
    if len(grid)<=0 or grid is None:
        return 0
    rows=len(grid)
    cols=len(grid[0])
    grid[0][0]=grid[0][0]
    # fill first row
    for col in range(1,cols):
        grid[0][col]=grid[0][col-1]+grid[0][col]
    # fill first col
    for row in range(1,rows):
        grid[row][0]=grid[row][0]+grid[row-1][0]
    
    for row in range(1,rows):
        for col in range(1,cols):
            grid[row][col]=grid[row][col]+ min(grid[row-1][col],grid[row][col-1])
    return grid[rows-1][cols-1]

    

print(minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))