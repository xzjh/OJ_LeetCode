class Solution:
	# @return a list of lists of integers
	def generate(self, numRows):
		ans = []
		for i in range(numRows):
			ans.append([])
			for j in range(i + 1):
				if j == 0 or j == i:
					ans[i].append(1)
				else:
					ans[i].append(ans[i - 1][j - 1] + ans[i - 1][j])
		return ans

s = Solution()
print s.generate(5)