# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def levelOrder(self, root):
		if not root:
			return []
		q = [root]
		qt = []
		res = []
		rest = []
		while q:
			node = q.pop(0)
			rest.append(node.val)
			if node.left:
				qt.append(node.left)
			if node.right:
				qt.append(node.right)
			if not q:
				q = qt
				qt = []
				res.append(rest)
				rest = []
		return res

s = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
print s.levelOrder(n1)