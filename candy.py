class Solution:
	# @param ratings, a list of integer
	# @return an integer
	def candy(self, ratings):
		if not ratings:
			return 0
		length = len(ratings)
		res = [1] * length
		for i in range(1, length):
			if ratings[i] > ratings[i - 1]:
				res[i] = res[i - 1] + 1
		for i in range(length - 1)[::-1]:
			if ratings[i] > ratings[i + 1]:
				res[i] = max(res[i], res[i + 1] + 1)
		return reduce(lambda x, y: x + y, res)

s = Solution()
print s.candy([4,2,3,4,1])