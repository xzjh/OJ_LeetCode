class Solution:
	# @param an integer
	# @return a list of string
	def generateParenthesis(self, n):

		def generate(left, right, ans, this_item):
			if left == 0 and right == 0:
				ans.append(this_item)
				return

			if left > 0:
				generate(left - 1, right, ans, this_item + '(')
			if left < right:
				generate(left, right - 1, ans, this_item + ')')

		ans = []
		generate(n, n, ans, '')
		return ans

s = Solution()
print s.generateParenthesis(1)