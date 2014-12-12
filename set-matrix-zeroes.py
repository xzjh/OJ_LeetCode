class Solution:
	# @param matrix, a list of lists of integers
	# RETURN NOTHING, MODIFY matrix IN PLACE.
	def setZeroes(self, matrix):
		if not matrix or not matrix[0]:
			return
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == 0:
					for i2 in range(len(matrix)):
						if matrix[i2][j] != 0:
							matrix[i2][j] = 1000000
					for j2 in range(len(matrix[0])):
						if matrix[i][j2] != 0:
							matrix[i][j2] = 1000000
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == 1000000:
					matrix[i][j] = 0
