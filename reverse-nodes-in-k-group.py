# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @param k, an integer
	# @return a ListNode
	def reverseKGroup(self, head, k):
		q1 = []
		q2 = []
		i = 0
		if head == None:
			return None
		this_node = head
		while this_node != None:
			q1.append(this_node)
			this_node = this_node.next
		while len(q1) >= k:
			for i in range(k)[::-1]:
				q2.append(q1.pop(i))
		q2.extend(q1)
		for i in range(1, len(q2)):
			q2[i - 1].next = q2[i]
		q2[i].next = None
		return q2[0]

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
s = Solution()
print s.reverseKGroup(n1, 3).val