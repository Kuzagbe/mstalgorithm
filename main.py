# THIS IS A REPRESENTATION OF THE PRIM'S MINIMUM SPANNNING TREE ALGORITHM
# WILL BE USING ADJACENCY MATRIX TO PRESENT THE GRAPH

import sys
class Graph():


	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]


	# THIS FUNCTION IS TO PRINT THE MST AND STORE IT IN THE PARENT[]
	def printMST(self, parent):
		print("Edge \tWeight")
		for i in range(1, self.V):
			print(parent[i], "-", i, "\t", self.graph[i][parent[i]])


	# A UTILITY FUNCTION TO FIND THE VERTEX WITH MINIMUM DISTANCE VALUE, FROM
	# THE SET OF VERTEX NOT YET INCLUDED IN SHORTEST PATH TREE
	def minKey(self, key, mstSet): # INITIALIZE THE MINIMUM VALUE
		minimum = sys.maxsize
		for v in range(self.V):
			if key[v] < minimum and mstSet[v] == False:
				minimum = key[v]
				minimum_index = v
		return minimum_index


	# PRINTING AND CONSTRUCTING THE MST GRAPH REPRESENTED USING ADJACENCY MATRIX
	def primMST(self):
		# VALUES USED TO CHOOSE THE MINIMUM WEIGHT EDGE
		key = [sys.maxsize] * self.V
		parent = [None] * self.V
		# ARRAY TO SAVE THE MST CONSTRUCTED
		key[0] = 0
		# MAKE KEY 0 SUCH THAT THE VERTEX IS PICKED AS THE FIRST VERTEX
		mstSet = [False] * self.V

		parent[0] = -1  # THE FIRST NODE CHOSEN WITH INDEX 0 IS SET TO MINUS 1

		for cout in range(self.V):
			# THIS IS TO PICK THE MINIMUM DISTANCE VERTICES THAT IS NOT PROCESSED
			u = self.minKey(key, mstSet)
			# INSERT THE MINIMUM VERTEX IN THE SHORTEST PATH TREE
			mstSet[u] = True
			for v in range(self.V):
				# UPDATE THE DISTANCE VALUE OF THE ADJACENT VERTICES OF THE PICKED VERTEX IF THE
				# CURRENT DISTANCE IS GREATER THAN THE NEW DISTANCE AND THE VERTEX IS NOT IN THE SHORTEST PATH
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
						key[v] = self.graph[u][v]
			# UPDATE THE KEY ONLY IF THE GRAPH [U][V] IS SMALLER THAN THE KEY[V]
						parent[v] = u

		self.printMST(parent)

g = Graph(7)
g.graph = [[0, 28, 0, 0, 0, 10, 0],
		[28, 0, 16, 0, 0, 0, 14],
		[0, 16, 0, 12, 0, 0, 0],
		[0, 0, 12, 0, 22, 0, 18],
		[0, 0, 0, 22, 0, 25, 24],
		[10, 0, 0, 0, 25, 0, 0],
		[0, 14, 0, 18, 24, 0, 0]]

g.primMST();
