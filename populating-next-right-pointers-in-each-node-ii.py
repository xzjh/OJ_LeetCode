# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		if not root:
			return
		next_node = None
		root_next = root.next
		while root_next and not next_node:
			if root_next.left:
				next_node = root_next.left
			else:
				next_node = root_next.right
			root_next = root_next.next

		if root.left:
			if root.right:
				root.left.next = root.right
			else:
				root.left.next = next_node
		if root.right:
			root.right.next = next_node

		self.connect(root.right)
		self.connect(root.left)