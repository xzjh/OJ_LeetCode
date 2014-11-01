class Solution:
	# @param s, a string
	# @return a boolean
	def isPalindrome(self, s):
		st = ''.join(ch for ch in s.lower() if ch.isalnum())
		length = len(st)
		for i in range(length / 2):
			if st[i] != st[length - 1 - i]:
				return False
		return True