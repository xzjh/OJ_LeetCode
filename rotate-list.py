# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param head, a ListNode
	# @param k, an integer
	# @return a ListNode
	def rotateRight(self, head, k):
		if not head:
			return None
		start = ListNode(-1)
		start.next = head
		node = head
		n = 1
		while node.next:
			node = node.next
			n += 1
		last_node = node
		r = k % n
		node = start
		if r > 0:
			for _ in range(n - r):
				node = node.next
			last_node.next = start.next
			start.next = node.next
			node.next = None
		return start.next
