# Definition for a undirected graph node
class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution:
	# @param node, a undirected graph node
	# @return a undirected graph node
	def cloneGraph(self, node):

		if not node:
			return node

		def iter(node, new_node, visited):
			if node.label in visited:
				return
			visited[node.label] = new_node
			for child in node.neighbors:
				if child.label in visited:
					new_child = visited[child.label]
				else:
					new_child = UndirectedGraphNode(child.label)
				new_node.neighbors.append(new_child)
				iter(child, new_child, visited)

		visited = {}
		new_root = UndirectedGraphNode(node.label)
		iter(node, new_root, visited)
		return new_root

s = Solution()
n1 = UndirectedGraphNode(1)
n2 = UndirectedGraphNode(2)
n3 = UndirectedGraphNode(3)
n1.neighbors.append(n2)
n1.neighbors.append(n3)
n2.neighbors.append(n3)
print s.cloneGraph(n1).neighbors[1].label