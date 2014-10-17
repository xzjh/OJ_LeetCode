class Solution:
	# @param num, a list of integer
	# @return an integer
	def findMin(self, num):
		if num == None or len(num) == 0:
			return None
		l = 0
		h = len(num) - 1
		p = (l + h) / 2
		while h - l > 1:
			if num[l] < num[p] and num[p] < num[h]:
				return num[l]
			elif num[l] > num[p]:
				h = p
			elif num[p] > num[h]:
				l = p
			p = (h + l) / 2
		return min(num[l], num[h])

s = Solution()
print s.findMin([1])