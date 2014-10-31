class Solution:
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSum(self, num):
		
		def twoSum(target, num):
			i = 0
			j = len(num) - 1
			res = []
			while i < j:
				if num[i] + num[j] == target:
					res.append([num[i], num[j]])
					i += 1
					j -= 1
					while i < j and num[i] == num[i - 1] and num[j] == num[j + 1]:
						i += 1
						j -= 1
				elif num[i] + num[j] < target:
					i += 1
				else:
					j -= 1
			return res

		res = []
		num_sorted = sorted(num)
		for i in range(len(num_sorted)):
			if i > 0 and num_sorted[i] == num_sorted[i - 1]:
				continue
			rr = twoSum(-num_sorted[i], num_sorted[i + 1:])
			for r in rr:
				res.append([num_sorted[i]] + r)
		return res

s = Solution()
print s.threeSum([0,0,0,1,-1,1,-1])
