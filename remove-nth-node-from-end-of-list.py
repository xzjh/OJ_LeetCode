# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @return a ListNode
	def removeNthFromEnd(self, head, n):
		
		start = ListNode(-1)
		start.next = head
		node = start
		ns = 0
		while node.next:
			node = node.next
			ns += 1
		i = 0
		node = start
		while i < (ns - n):
			node = node.next
			i += 1
		node.next = node.next.next
		return start.next
