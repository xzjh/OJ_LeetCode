class Solution:
	# @param triangle, a list of lists of integers
	# @return an integer
	def minimumTotal(self, triangle):
		if not triangle:
			return None
		dp = list(triangle[-1])
		for i in range(len(triangle) - 1)[::-1]:
			for j in range(i + 1):
				dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

		return dp[0]

s = Solution()
t = [ \
     [2], \
    [3,4], \
   [6,5,7], \
  [4,1,8,3] \
]
print s.minimumTotal(t)