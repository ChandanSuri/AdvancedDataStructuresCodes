# Chandan Suri
# 101403054

from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)
		
	def addEdge(self, v, w):
		self.graph[v].append(w)
	
	def printGraph(self):
		print(self.graph.items())
	
	def getPath(self, path):
		p = ""
		for v in path:
			p += "%d -> " % v
		return p[:len(p)-3]
	
	def dfs(self):
		length = len(self.graph)
		visited = [False] * (length)
		path = []
		
		for i in range(length):
			if visited[i] == False:
				self.dfsiter(path, i, visited)
		print(self.getPath(path))
		
	def dfsiter(self, path, v, visited):
		visited[v] = True
		path.append(v)
		for i in self.graph[v]:
			if visited[i] == False:
				self.dfsiter(path, i, visited)
	
	def printNeighbor(self, node):
		if self.graph[node]:
			print(self.graph[node])
			
g_obj = Graph()
n_ele = input("Enter the no. of elememts to be inserted: ")
for i in range(int(n_ele)):
	v = input("Enter v : ")
	w = input("Enter w : ")
	g_obj.addEdge(v, w)
	g_obj.addEdge(w, v)
print("Grapgh: ")
g_obj.printGraph()
print("DFS: ")
g_obj.dfs()
s_neighbor = input("Enter the Node for which neighbors to be retrieved: ")
g_obj.printNeighbor(s_neighbor)
	