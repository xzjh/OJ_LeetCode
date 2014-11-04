# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return nothing, do it in place
	def flatten(self, root):
		if not root:
			return root
		if not root.left:
			if root.right:
				return self.flatten(root.right)
			else:
				return root
		else:
			left_last_leaf = self.flatten(root.left)
			root_right = root.right
			root.right = root.left
			root.left = None
			left_last_leaf.right = root_right
			if root_right:
				return self.flatten(root_right)
			else:
				return left_last_leaf