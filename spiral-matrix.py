class Solution:
	# @param matrix, a list of lists of integers
	# @return a list of integers
	def spiralOrder(self, matrix):
		if not matrix:
			return []
		m = len(matrix)
		n = len(matrix[0])
		t = 0
		res = []
		while t < min(m, n) / 2:
			for j in range(t, n - t - 1):
				res.append(matrix[t][j])
			for i in range(t, m - t - 1):
				res.append(matrix[i][n - t - 1])
			for j in range(t + 1, n - t)[::-1]:
				res.append(matrix[m - t - 1][j])
			for i in range(t + 1, m - t)[::-1]:
				res.append(matrix[i][t])
			t += 1
		if min(m, n) % 2 == 1:
			if m < n:
				res.extend(matrix[t][t:n - t])
			else:
				for i in range(t, m - t):
					res.append(matrix[i][t])
		return res
