class Solution:
	# @param {integer[][]} matrix
	# @param {integer} target
	# @return {boolean}
	def searchMatrix(self, matrix, target):

		if not matrix:
			return False
		nrow = len(matrix)
		ncol = len(matrix[0])
		for i in range(nrow):
			if matrix[i][0] <= target and matrix[i][ncol - 1] >= target:
				low = 0
				high = ncol - 1
				while low <= high:
					j = (low + high) / 2
					if matrix[i][j] == target:
						return True
					elif matrix[i][j] > target:
						high = j - 1
					else:
						low = j + 1
		return False
