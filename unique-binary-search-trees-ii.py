# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @return a list of tree node
	def generateTrees(self, n):
		
		def iter(l):
			if not l:
				return [None]
			res = []
			for i in range(len(l)):
				node_left = iter(l[:i])
				node_right = iter(l[i + 1:])
				for k in range(len(node_left)):
					for h in range(len(node_right)):
						node = TreeNode(l[i])
						node.left = node_left[k]
						node.right = node_right[h]
						res.append(node)
			return res
		return iter(range(1, n + 1))

s = Solution()
print s.generateTrees(5)[0].val