class Solution:
	# @return an integer
	def numTrees(self, n):

		ans = {}

		def iter(n):
			if n in ans:
				return ans[n]
			s = 0
			for i in range(n):
				s += iter(i) * iter(n - i - 1)
			ans[n] = s
			return s

		ans[0] = 1
		ans[1] = 1
		return iter(n)

s = Solution()
print s.numTrees(4)