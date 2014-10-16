# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def deleteDuplicates(self, head):
		if head == None:
			return None
		cur = head
		next_node = head.next
		while next_node != None:
			if next_node.val == cur.val:
				cur.next = next_node.next
			else:
				cur = next_node
			next_node = next_node.next

		return head

s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)
n4 = ListNode(2)
n1.next = n2
n2.next = n3
n3.next = n4
print s.deleteDuplicates(n1).next.val