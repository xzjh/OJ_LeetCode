class Solution:
	# @param num, a list of integer
	# @return a list of lists of integers
	def permute(self, num):
		
		def iter(item, num):
			if not num:
				res.append(item)
				return
			for i in range(len(num)):
				iter(item + [num[i]], num[:i] + num[i + 1:])
		
		res = []
		iter([], num)
		return res

s = Solution()
print s.permute([1,2,3])
