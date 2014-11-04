# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param head, a list node
	# @return a tree node
	def sortedListToBST(self, head):
		
		def iter(start, end):
			if start == end:
				return None
			first = start
			second = start
			while second != end and second.next != end:
				first = first.next
				second = second.next.next
			root_node = TreeNode(first.val)
			root_node.left = iter(start, first)
			root_node.right = iter(first.next, end)
			return root_node
		
		if not head:
			return None
	
		return iter(head, None)