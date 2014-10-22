class Solution:
	# @return a list of integers
	def getRow(self, rowIndex):
		a = [0] * (rowIndex + 1)
		b = [0] * (rowIndex + 1)
		for i in range(rowIndex + 1):
			if i % 2:
				l = b
				l2 = a
			else:
				l = a
				l2 = b
			for j in range(i + 1):
				if j == 0 or j == i:
					l[j] = 1
				else:
					l[j] = l2[j - 1] + l2[j]
		return l[:rowIndex + 2]

s = Solution()
print s.getRow(3)