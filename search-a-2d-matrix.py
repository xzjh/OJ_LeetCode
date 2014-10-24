class Solution:
	# @param matrix, a list of lists of integers
	# @param target, an integer
	# @return a boolean
	def searchMatrix(self, matrix, target):
		
		def get_value(index):
			 row = index // row_length
			 col = index % row_length
			 return matrix[row][col]

		if not matrix:
			return False

		row_length = len(matrix[0])
		length = row_length * len(matrix)
		high = length - 1
		low = 0
		while high >= low:
			i = (high + low) / 2
			v = get_value(i)
			if v == target:
				return True
			elif v > target:
				high = i - 1
			else:
				low = i + 1

		return False

s = Solution()
m = [ \
  [1,   3,  5,  7], \
  [10, 11, 16, 20], \
  [23, 30, 34, 50] \
]
print s.searchMatrix(m,3)