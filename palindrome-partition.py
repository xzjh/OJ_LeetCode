class Solution:
	# @param s, a string
	# @return a list of lists of string
	def partition(self, s):

		def is_palindrome(s):
			if len(s) < 2:
				return True
			l = 0
			r = len(s) - 1
			while r > l:
				if s[r] != s[l]:
					return False
				r -= 1
				l += 1
			return True
		
		def dfs(s, output, result):
			if len(s) == 0:
				result.append(output)
				return
			for i in range(len(s)):
				if is_palindrome(s[:i + 1]):
					new_output = list(output)
					new_output.append(s[:i + 1])
					dfs(s[i + 1:], new_output, result)

		result = []
		dfs(s, [], result)
		return result

s = Solution()
print s.partition('aab')