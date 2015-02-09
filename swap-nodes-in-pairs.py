# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param a ListNode
	# @return a ListNode
	def swapPairs(self, head):
		if not head:
			return None
		this_node = head
		if this_node.next:
			head = this_node.next
		prev_node = ListNode(-1)
		while this_node and this_node.next:
			next_node = this_node.next
			this_node.next = next_node.next
			next_node.next = this_node
			prev_node.next = next_node
			prev_node = this_node
			this_node = this_node.next
		return head

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
s = Solution()
print s.swapPairs(n1).next.val