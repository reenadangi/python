adj_list={
    "A":["B","C"],
    "B":["A","D"],
    "C":["A","D","E"],
    "D":["B","C","E"],
    "E":["C","D"]
}
class Graph:
    def __init__(self,Nodes,is_directed=True):
      self.nodes=Nodes
      self.adj_list={}
      self.is_directed=is_directed
      for node in self.nodes:
          self.adj_list[node]=[]
    def print_adj_list(self):
        for node in self.adj_list:
            print (f"{node} => {self.adj_list[node]}")
    def add_edge(self,u,v):
        
        self.adj_list[u].append(v)
        if not self.is_directed:
            self.adj_list[v].append(u) 
    def dgree(self,u):
        # how many adj/connected nodes are there for that node
        return len(self.adj_list[u])
    def dfs(self):
        color={}
        parent={}
        travel_time={}
        dfs_traversal_output=[]

        for node in self.adj_list.keys():
            color[node]="W"
            parent[node]=None
            travel_time[node]=[-1,-1]
        print(color,parent,travel_time)  
        def dfs_util(u):
            color[u]="G"       

nodes=["A","B","C","D","E"]    
all_edges=[
    ("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E")
]
graph=Graph(nodes)
graph.print_adj_list()
for u,v in all_edges: 
    graph.add_edge(u,v)
graph.print_adj_list()
print(graph.dgree("D"))
graph.dfs()
