# Definition for singly-linked list with a random pointer.
class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution:
	# @param head, a RandomListNode
	# @return a RandomListNode
	def copyRandomList(self, head):

		if not head:
			return head

		d = {}
		node = head
		while node:
			d[node] = RandomListNode(node.label)
			node = node.next
		for old, new in d.iteritems():
			if old.next:
				new.next = d[old.next]
			if old.random:
				new.random = d[old.random]
		return d[head]

s = Solution()
n1 = RandomListNode(1)
n2 = RandomListNode(2)
n3 = RandomListNode(3)
n1.next = n2
n2.next = n3
print s.copyRandomList(n1).label