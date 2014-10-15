# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param head, a ListNode
	# @return a boolean
	def hasCycle(self, head):
		if head == None or head.next == None:
			return False
		a = head
		b = head
		while a.next!= None and a.next.next != None:
			a = a.next.next
			b = b.next
			if a == b:
				return True
		return False