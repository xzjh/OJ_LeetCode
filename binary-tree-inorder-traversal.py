# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def inorderTraversal(self, root):
		
		output = []
		stack = []
		node = root
		while node:
			while node:
				stack.append(node)
				node = node.left
			while stack:
				node = stack.pop()
				output.append(node.val)
				node = node.right
				if node:
					break
				else:
					continue
		return output

s = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.right = n3
print s.inorderTraversal(n1)