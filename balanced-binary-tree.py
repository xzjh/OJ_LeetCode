# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isBalanced(self, root):

		if not root:
			return True

		return self.get_height(root) != -1

	def get_height(self, root):
		if not root:
			return 0
		left_height = self.get_height(root.left)
		right_height = self.get_height(root.right)
		if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
			return -1
		else:
			return max(left_height, right_height) + 1

s = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2
n2.right = n3
n3.right = n4
n4.right = n5
print s.isBalanced(n1)
