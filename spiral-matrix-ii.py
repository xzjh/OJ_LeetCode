class Solution:
	# @return a list of lists of integer
	def generateMatrix(self, n):
		if n <= 0:
			return []
		matrix = [[0] * n for _ in range(n)]
		t = 0
		res = []
		r = 1
		while t < n / 2:
			for j in range(t, n - t - 1):
				matrix[t][j] = r
				r += 1
			for i in range(t, n - t - 1):
				matrix[i][n - t - 1] = r
				r += 1
			for j in range(t + 1, n - t)[::-1]:
				matrix[n - t - 1][j] = r
				r += 1
			for i in range(t + 1, n - t)[::-1]:
				matrix[i][t] = r
				r += 1
			t += 1
		if n % 2 == 1:
			matrix[t][t] = r
		return matrix
