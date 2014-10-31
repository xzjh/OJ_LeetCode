# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param inorder, a list of integers
	# @param postorder, a list of integers
	# @return a tree node
	def buildTree(self, inorder, postorder):
		
		if len(postorder) == 0:
			return None
		if len(postorder) == 1:
			return TreeNode(postorder[0])
		root_val = postorder[-1]
		i = 0
		while inorder[i] != root_val:
			i += 1
		inorder_left = inorder[:i]
		inorder_right = inorder[i + 1:]
		left_length = len(inorder_left)
		right_length = len(inorder_right)
		root = TreeNode(root_val)
		if len(inorder_left) > 0:
			root.left = self.buildTree(inorder_left, postorder[: left_length])
		if len(inorder_right) > 0:
			root.right = self.buildTree(inorder_right, postorder[left_length: -1])
		return root

s = Solution()
print s.buildTree([1,2,3,4,5,6], [2,1,5,4,6,3]).val