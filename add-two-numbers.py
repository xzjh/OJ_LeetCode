# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @return a ListNode
	def addTwoNumbers(self, l1, l2):
		if not l1 or not l2:
			return None
		head = ListNode((l1.val + l2.val) % 10)
		node = head
		cur1 = l1.next
		cur2 = l2.next
		carry = (l1.val + l2.val) // 10
		while cur1 and cur2:
			this_sum = cur1.val + cur2.val + carry
			new_node = ListNode(this_sum % 10)
			carry = this_sum // 10
			node.next = new_node
			cur1 = cur1.next
			cur2 = cur2.next
			node = new_node
		cur = cur1 if cur1 else cur2
		while cur:
			this_sum = cur.val + carry
			new_node = ListNode(this_sum % 10)
			carry = this_sum // 10
			node.next = new_node
			cur = cur.next
			node = new_node
		if carry:
			new_node = ListNode(carry)
			node.next = new_node
		return head
		