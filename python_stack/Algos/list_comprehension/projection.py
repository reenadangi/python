 Projection Area of 3D Shapes
#  def projectionArea(self, grid: List[List[int]]) -> int:
#         front = sum(max(i) for i in zip(*grid))
#         top = sum(1 for i in grid for j in i if j)
#         side = sum(max(i) for i in grid)
#         return front + top + side     