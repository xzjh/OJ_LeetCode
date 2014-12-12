# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def deleteDuplicates(self, head):
		
		if not head:
			return head
		
		start = ListNode(-1)
		start.next = head
		left = start
		right = head
		is_dup = False
		while right:
			while right.next and right.val == right.next.val:
				right = right.next
				is_dup = True
			if not is_dup:
				left.next = right
				left = left.next
			right = right.next
			is_dup = False
		left.next = None
		return start.next
