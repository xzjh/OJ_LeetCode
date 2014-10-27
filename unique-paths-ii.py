class Solution:
	# @param obstacleGrid, a list of lists of integers
	# @return an integer
	def uniquePathsWithObstacles(self, obstacleGrid):
		
		if obstacleGrid[0][0] == 1:
			return 0

		row_num = len(obstacleGrid)
		col_num = len(obstacleGrid[0])
		if obstacleGrid[0][0] == 1:
			return 0

		dp = [[0] * col_num for _ in range(row_num)]
		dp[0][0] = 1
		for i in range(row_num):
			for j in range(col_num):
				if obstacleGrid[i][j] == 1:
					continue
				if i - 1 >= 0:
					dp[i][j] += dp[i - 1][j]
				if j - 1 >= 0:
					dp[i][j] += dp[i][j - 1]
		return dp[row_num - 1][col_num - 1]

s = Solution()
g = [ 
  [0,0,0], 
  [0,1,0], 
  [0,0,0] 
]
print s.uniquePathsWithObstacles(g)