# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {string[]}
	def binaryTreePaths(self, root):
		
		def helper(node, res_item):
			if node.left:
				helper(node.left, res_item + '->' + str(node.left.val))
			if node.right:
				helper(node.right, res_item + '->' + str(node.right.val))
			if not node.left and not node.right:
				res.append(res_item)
		
		res = []
		if root:
			helper(root, str(root.val))
		return res
