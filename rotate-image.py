class Solution:
	# @param matrix, a list of lists of integers
	# @return a list of lists of integers
	def rotate(self, matrix):
		if not matrix:
			return matrix
		n = len(matrix)
		for i in range(n // 2):
			for j in range(i, n - 1 - i):
				t = matrix[i][j]
				matrix[i][j] = matrix[n - 1 - j][i]
				matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
				matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
				matrix[j][n - 1 - i] = t
		return matrix
