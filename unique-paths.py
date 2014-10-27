class Solution:
	# @return an integer
	def uniquePaths(self, m, n):
		
		def c(n, m):
			if m == 0:
				return 1
			return reduce(lambda x, y: x * y, range(n - m + 1, n + 1)) / \
				reduce(lambda x, y: x * y, range(1, m + 1))

		return c(m + n - 2, min(m, n) - 1)

s = Solution()
print s.uniquePaths(1,2)