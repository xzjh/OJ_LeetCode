# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def insertionSortList(self, head):
		if not head:
			return None
		start = ListNode(0)
		start.next = head
		cur_node = head
		while cur_node.next:
			pre_node = start
			while pre_node != cur_node:
				if pre_node.next.val > cur_node.next.val:
					temp1 = pre_node.next
					temp2 = cur_node.next.next
					pre_node.next = cur_node.next
					cur_node.next.next = temp1
					cur_node.next = temp2
					break
				else:
					pre_node = pre_node.next
			if pre_node == cur_node:
				cur_node = cur_node.next
		return start.next

n1 = ListNode(4)
n2 = ListNode(1)
n3 = ListNode(3)
n4 = ListNode(2)
n1.next = n2
n2.next = n3
n3.next = n4
s = Solution()
print s.insertionSortList(n1).val