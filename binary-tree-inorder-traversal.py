# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def inorderTraversal(self, root):
		
		output = []
		stack = []
		node = root
		while stack or node:
			while node:
				stack.append(node)
				node = node.left
			if stack:
				node = stack.pop()
				output.append(node.val)
				node = node.right
		return output
		