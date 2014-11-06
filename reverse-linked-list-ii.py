# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param head, a ListNode
	# @param m, an integer
	# @param n, an integer
	# @return a ListNode
	def reverseBetween(self, head, m, n):
		if not head:
			return None
		start = ListNode(-1)
		start.next = head
		node = start
		i = 1
		while i < m:
			node = node.next
			i += 1
		prev_first = node
		node = node.next
		first_node = node
		node_prev = node
		node_next = node.next
		i += 1
		while i <= n:
			node = node_next
			node_next = node.next
			node.next = node_prev
			node_prev = node
			i += 1
		last_node = node
		prev_first.next = last_node
		first_node.next = node_next
		return start.next
		