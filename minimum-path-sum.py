class Solution:
	# @param grid, a list of lists of integers
	# @return an integer
	def minPathSum(self, grid):
		if not grid:
			return 0
		row_num = len(grid)
		col_num = len(grid[0])
		dp = [[0] * col_num for _ in range(row_num)]
		dp[0][0] = grid[0][0]
		for i in range(1, row_num):
			dp[i][0] = dp[i - 1][0] + grid[i][0]
		for j in range(1, col_num):
			dp[0][j] = dp[0][j - 1] + grid[0][j]
		for i in range(1, row_num):
			for j in range(1, col_num):
				dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
		return dp[row_num - 1][col_num - 1]