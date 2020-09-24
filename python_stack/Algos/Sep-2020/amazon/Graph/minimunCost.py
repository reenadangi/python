class Solution(object):
   def find(self, x):
      if self.parent[x] == -1:
         return x
      self.parent[x] = self.find(self.parent[x])
      return self.parent[x]
   def union(self,x,y):
      parent_x = self.find(x)
      parent_y = self.find(y)
      if parent_x == parent_y:
         return
      self.parent[parent_y] = parent_x
   def minimumCost(self, n, connections):
      self.parent = [ -1 for i in range(n+1)]
      disjoint = n-1
      cost = 0
      c = sorted(connections,key=lambda v:v[2])
      i = 0
      while i<len(c) and disjoint:
         x = c[i][0]
         y = c[i][1]
         if self.find(x)!=self.find(y):
            disjoint-=1
            cost+=c[i][2]
            self.union(x,y)
            i+=1
         return cost if not disjoint else -1
ob = Solution()
print(ob.minimumCost(3, [[1,2,5], [1,3,6], [2,3,1]]))