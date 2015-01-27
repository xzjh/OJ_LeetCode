# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def postorderTraversal(self, root):
		
		if not root:
			return []
		res = []
		stack = []
		node = root
		pre = None
		while node or stack:
			while node:
				stack.append(node)
				node = node.left
			if stack:
				node_t = stack[-1]
				if node_t.right and node_t.right != pre:
					node = node_t.right
				else:
					res.append(node_t.val)
					pre = node_t
					stack.pop()
		return res
