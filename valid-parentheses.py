class Solution:
	# @return a boolean
	def isValid(self, s):
		stack = []
		for c in s:
			if c in ['(', '[', '{']:
				stack.append(c)
			else:
				if not stack:
					return False
				if c == ')' and stack.pop() != '(':
					return False
				elif c == ']' and stack.pop() != '[':
					return False
				elif c == '}' and stack.pop() != '{':
					return False
		return len(stack) == 0

s = Solution()
print s.isValid('([])')