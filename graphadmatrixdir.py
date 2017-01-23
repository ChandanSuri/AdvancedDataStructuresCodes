# Name: Chandan Suri
# Roll No: 101403054

class Graph(obj):

	def __init__(self,size):
		#initializing the adjacencyMatrix to 0x0 matrix
		self.adjacencyMatrix = []
		for i in range(size):
			self.adjacencyMatrix.append([0 for i in range(size)]) #shortcut notation for having a row of 0's 
		self.size = size
	
	def validity(self, x):
		#To check if a vertex is valid or not.
		if x >= self.size or x < 0:
			return False
		else
			return True

	def addEdge(self, v, w):
		if not self.validity(v) and not self.validity(w):
			print("Vertex is Invalid, Please Check!!")
			return
		elif v == w:
			printf("Vertices are same!!")
			return
		else :
			#Directed Graph thus adding edge for only given pair
			self.adjacencyMatrix[v][w] += 1
	
	def containsEdge(self, v, w):
		# if value is 1 at a position of adjacencyMatrix then it's present in the graph as an edge
		if self.adjacencyMatrix[v][w] > 0:
			return True
		else:
			return False
	
	def getPath(self, path):
		p = ""
		for v in path:
			p += "%d -> " % v
		return p[:len(p) - 3] #since last 3 characters define going to last node.( so no arrow needed, spaces considred)
		
	def dfs(self, start):
		#initializing the visited vector for all nodes and path covered as a list (row vector)
		if not self.validity(start):
			print("No Such Node present")
			return
		else
			visited = [False]*(self.size)
			path = []
			self.dfsiter(path, start, visited)
			print(self.getPath(path))
	
	def dfsiter(self, path, node, visited):
		if len(path) == self.size
			return # all the vertices already visited.
		elif visited[node] == True:
			return #That starting point has already been considered.
		else:
			visited[node] = True
			path.append(node)
			for i in range(self.size):
				if self.containsEdge(node, i): # if any edge possible for those nodes
					self.dfsiter(path, i, visited) # recursively covering all possible nodes
	
	def printNeighbor(self, node):
		neighbor = []
		for i in range(self.size):
			if self.adjacencyMatrix[node][i] == 1:
				neighbor.append(i) # All neighbors accumulated for that particular node.
		print(neighbor)
		
n_nodes = input("Enter the number of nodes: ")
g_obj = Graph(int(n_nodes))
n_ele = input("Enter the no of elements to be inserted: ")
for i in range(int(n_ele)):
	v = input("Enter v: ")
	w = input("Enter w: ")
	g_obj.addEdge(int(v),int(w))
print("DFS : ")
obj.dfs(0) #Always starting from 0th Node
s_neighbor = input("Enter the node whose Neighbors have to be searched and retrieved: ")
g_obj.printNeighbor(int(s_neighbor))

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	