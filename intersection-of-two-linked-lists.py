# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param two ListNodes
	# @return the intersected ListNode
	def getIntersectionNode(self, headA, headB):
		
		if not headA or not headB:
			return None
		
		lenA = 1
		lenB = 1
		nodeA = headA
		nodeB = headB
		while nodeA.next:
			nodeA = nodeA.next
			lenA += 1
		while nodeB.next:
			nodeB = nodeB.next
			lenB += 1
		nodeA = headA
		nodeB = headB
		if lenA > lenB:
			diff = lenA - lenB
			for _ in range(diff):
				nodeA = nodeA.next
		elif lenA < lenB:
			diff = lenB - lenA
			for _ in range(diff):
				nodeB = nodeB.next
		while nodeA and nodeB and nodeA != nodeB:
			nodeA = nodeA.next
			nodeB = nodeB.next
		if nodeA and nodeB:
			return nodeA
		else:
			return None
