# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
		if head == None or head.next == None:
			return None
		a = head
		b = head
		while a.next!= None and a.next.next != None:
			a = a.next.next
			b = b.next
			if a == b:
				b = head
				while True:
					if a == b:
						return a
					a = a.next
					b = b.next
		return None