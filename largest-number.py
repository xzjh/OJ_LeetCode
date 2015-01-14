class Solution:
	# @param num, a list of integers
	# @return a string
	def largestNumber(self, num):
		nums = map(str, num)
		nums.sort(cmp = lambda x, y: cmp(y + x, x + y))
		ret = ''.join(nums)
		return ret.lstrip('0') or '0'
