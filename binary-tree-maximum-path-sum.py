# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def __init__(self):
		self.max_sum = -10000000

	def maxPathSum(self, root):

		def iter(root):
			if root == None:
				return 0
			left_sum = iter(root.left)
			right_sum = iter(root.right)
			one_path = max(root.val, max(left_sum, right_sum) + root.val)
			arch_path = left_sum + root.val + right_sum
			self.max_sum = max(self.max_sum, one_path, arch_path)
			return one_path

		self.max_sum = max(iter(root), self.max_sum)
		return self.max_sum

s = Solution()
n1 = TreeNode(-2)
n2 = TreeNode(6)
n3 = TreeNode(0)
n4 = TreeNode(-6)
n1.left = n2
n2.left = n3
n2.right = n4
print s.maxPathSum(n1)