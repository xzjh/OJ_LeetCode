# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return nothing
	def reorderList(self, head):
		if head ==  None:
			return None
		stack = [head]
		next_node = head.next
		while next_node != None:
			stack.append(next_node)
			next_node = next_node.next
		cur_node = stack.pop(0)
		while len(stack) > 1:
			cur_node.next = stack.pop()
			cur_node = cur_node.next
			cur_node.next = stack.pop(0)
			cur_node = cur_node.next

		if len(stack) == 1:
			cur_node.next = stack.pop()
			cur_node = cur_node.next

		cur_node.next = None

		return head

s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
#n1.next = n2
n2.next = n3
n3.next = n4
print s.reorderList(n1).val