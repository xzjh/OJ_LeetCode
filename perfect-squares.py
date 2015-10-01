class Solution(object):
	dp = [0]
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		dp = self.dp
		while len(dp) <= n:
			dp += min(dp[-k * k] for k in range(1, int(len(dp) ** 0.5) + 1)) + 1,
		return dp[n]
