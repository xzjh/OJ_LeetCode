# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param preorder, a list of integers
	# @param inorder, a list of integers
	# @return a tree node
	def buildTree(self, preorder, inorder):
		
		if len(preorder) == 0:
			return None
		if len(preorder) == 1:
			return TreeNode(preorder[0])
		root_val = preorder[0]
		i = 0
		while inorder[i] != root_val:
			i += 1
		inorder_left = inorder[:i]
		inorder_right = inorder[i + 1:]
		left_length = len(inorder_left)
		right_length = len(inorder_right)
		root = TreeNode(root_val)
		if len(inorder_left) > 0:
			root.left = self.buildTree(preorder[1: left_length + 1], inorder_left)
		if len(inorder_right) > 0:
			root.right = self.buildTree(preorder[1 + left_length:], inorder_right)
		return root

s = Solution()
print s.buildTree([1,2,3,4,5],[3,2,4,1,5]).val