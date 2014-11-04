# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a tree node
	def recoverTree(self, root):
		
		if not root:
			return None
		
		first = None
		second = None
		node = root
		last_node = TreeNode(-100000)
		last_node.right = root
		flag = 1
		while node:
			if node.left:
				node_t = node.left
				while node_t.right and node_t != last_node:
					node_t = node_t.right
				if last_node == node_t:
					# second time, remove link
					last_node.right = None
				else:
					# first time, create link
					node_t.right = node
					node = node.left
					continue
			# visit
			if last_node.val > node.val:
				if flag == 1:
					first = last_node
					second = node
					flag = 2
				else:
					second = node
			last_node = node
			node = node.right

		if first and second:
			first.val, second.val = second.val, first.val
		return root

s = Solution()
# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(6)
# n5 = TreeNode(4)
# n6 = TreeNode(9)
# n1.right = n2
# n2.left = n3
# n2.right = n6
# n3.left = n4
# n3.right = n5
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
print s.recoverTree(n1).left.val
