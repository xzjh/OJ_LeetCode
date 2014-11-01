# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def sumNumbers(self, root):
		
		def iter(root, num):
			if not root.left and not root.right:
				nums.append(num * 10 + root.val)
				return
			if root.left:
				iter(root.left, num * 10 + root.val)
			if root.right:
				iter(root.right, num * 10 + root.val)
		
		if not root:
			return 0
		nums = []
		iter(root, 0)
		return reduce(lambda x, y: x + y, nums)