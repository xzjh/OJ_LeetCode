# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param num, a list of integers
	# @return a tree node
	def sortedArrayToBST(self, num):

		length = len(num)
		
		if length == 0:
			return None
		if length == 1:
			return TreeNode(num[0])
		else:
			root = length // 2
			root_node = TreeNode(num[root])
			root_node.left = self.sortedArrayToBST(num[:root])
			root_node.right = self.sortedArrayToBST(num[root + 1:])
			return root_node

s = Solution()
print s.sortedArrayToBST([1,3]).val
