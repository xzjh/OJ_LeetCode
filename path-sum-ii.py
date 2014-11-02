# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @param sum, an integer
	# @return a list of lists of integers
	def pathSum(self, root, sum):

		def iter(root, sum, res_item):
			if not root:
				return
			res_item.append(root.val)
			if not root.left and not root.right:
				if sum == root.val:
					res.append(res_item)
			else:
				iter(root.left, sum - root.val, list(res_item))
				iter(root.right, sum - root.val, list(res_item))
		
		res = []
		iter(root, sum, [])
		return res