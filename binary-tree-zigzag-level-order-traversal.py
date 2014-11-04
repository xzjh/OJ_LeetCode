# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def zigzagLevelOrder(self, root):
		
		if not root:
			return []
		q = [root]
		next_q = []
		res = []
		res_level = []
		depth = 0
		while q:
			node = q.pop(0)
			res_level.append(node.val)
			if node.left:
				next_q.append(node.left)
			if node.right:
				next_q.append(node.right)
			if not q:
				if depth % 2 == 1:
					res_level.reverse()
				res.append(res_level)
				res_level = []
				q = next_q
				next_q = []
				depth += 1
		return res
