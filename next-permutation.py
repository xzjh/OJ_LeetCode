class Solution:
	# @param num, a list of integer
	# @return a list of integer
	def nextPermutation(self, num):
		if not num:
			return num
		length = len(num)
		violate = length - 2
		while violate >= 0:
			if num[violate] < num[violate + 1]:
				break
			violate -= 1
		if violate >= 0:
			for right in range(length)[::-1]:
				if num[right] > num[violate]:
					break
			num[violate], num[right] = num[right], num[violate]
		for i in range((length - violate) / 2):
			num[violate + 1 + i], num[length - i - 1] = \
				num[length - i - 1], num[violate + 1 + i]
		return num

s = Solution()
print s.nextPermutation([5,1,1])