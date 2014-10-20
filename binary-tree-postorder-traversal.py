# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def postorderTraversal(self, root):

		def iter(root, ans):
			if not root:
				return
			iter(root.left, ans)
			iter(root.right, ans)
			ans.append(root.val)

		ans = []
		iter(root, ans)
		return ans

s = Solution()
r = TreeNode(1)
l = TreeNode(2)
i = TreeNode(3)
r.left = l
r.right = i
print s.postorderTraversal(r)