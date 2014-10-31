class Solution:
	# @param num, a list of integer
	# @return an integer
	def findMin(self, num):
		if num == None or len(num) == 0:
			return None
		l = 0
		h = len(num) - 1
		while h >= l:
			p = (h + l) / 2
			if num[l] <= num[p] and num[p] <= num[h]:
				return num[l]
			elif num[l] > num[p]:
				h = p
				l += 1
			elif num[p] > num[h]:
				l = p + 1
		return num[p]

s = Solution()
print s.findMin([2,1])