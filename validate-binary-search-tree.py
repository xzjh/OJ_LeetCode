# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isValidBST(self, root):
		
		def iter(root, min, max):
			if not root:
				return True
			if root.val >= max or root.val <= min:
				return False
			return iter(root.left, min, root.val) and iter(root.right, root.val, max)
		
		return iter(root, -100000, 100000)