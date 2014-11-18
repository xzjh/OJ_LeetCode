# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param a list of ListNode
	# @return a ListNode
	def mergeKLists(self, lists):
		def sort_list(list_a, list_b):
			if not list_a:
				return list_b
			elif not list_b:
				return list_a
			start = ListNode(-1)
			node_a = list_a
			node_b = list_b
			node = start
			while node_a and node_b:
				if node_a.val > node_b.val:
					node.next = node_b
					node = node_b
					node_b = node_b.next
				else:
					node.next = node_a
					node = node_a
					node_a = node_a.next
			if node_a:
				node.next = node_a
			if node_b:
				node.next = node_b
			
			return start.next
			
		if not lists:
			return None
		
		while len(lists) >= 2:
			new_list = []
			while len(lists) >= 2:
				list_a = lists.pop()
				list_b = lists.pop()
				new_list.append(sort_list(list_a, list_b))
			new_list.extend(lists)
			lists = new_list
		return lists[0]
		
s = Solution()
n1 = ListNode(2)
n2 = ListNode(-1)
print s.mergeKLists([n1,None,n2])
