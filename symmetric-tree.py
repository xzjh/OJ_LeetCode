# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isSymmetric(self, root):
		
		def isSym(root1, root2):
			if not root1 or not root2:
				return root1 == root2
			elif root1.val == root2.val:
				return isSym(root1.left, root2.right) and isSym(root1.right, root2.left)
			else:
				return False
				
		if not root:
			return True
		return isSym(root.left, root.right)