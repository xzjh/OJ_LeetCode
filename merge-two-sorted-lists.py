# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param two ListNodes
	# @return a ListNode
	def mergeTwoLists(self, l1, l2):
		if not l1 and not l2:
			return None
		start = ListNode(-1)
		node = start
		cur1 = l1
		cur2 = l2
		while cur1 and cur2:
			if cur1.val < cur2.val:
				node.next = cur1
				cur1 = cur1.next
			else:
				node.next = cur2
				cur2 = cur2.next
			node = node.next
		cur = cur1 if cur1 else cur2
		if cur:
			node.next = cur
		return start.next
