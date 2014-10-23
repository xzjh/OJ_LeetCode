# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @param x, an integer
	# @return a ListNode
	def partition(self, head, x):
		if not head:
			return head
		start = ListNode(0)
		start.next = head
		first = start
		while first.next and first.next.val < x:
			first = first.next
		second = first.next
		while second and second.next:
			if second.next.val < x:
				temp = second.next
				second.next = second.next.next
				temp.next = first.next
				first.next = temp
				first = first.next
			else:
				second = second.next
		return start.next

s = Solution()
n1 = ListNode(2)
n2 = ListNode(1)
n3 = ListNode(1)
n4 = ListNode(2)
n1.next = n2
# n2.next = n3
# n3.next = n4
print s.partition(n1,2).val