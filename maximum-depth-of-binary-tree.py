# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def maxDepth(self, root):
		
		def iter(root, depth):
			if not root:
				return depth
			return max(iter(root.left, depth + 1), iter(root.right, depth + 1))
			
		if not root:
			return 0
		
		return iter(root, 0)