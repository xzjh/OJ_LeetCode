class Solution(object):
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums) + 1
		r = reduce(lambda x, y: x ^ y, range(n))
		s = reduce(lambda x, y: x ^ y, nums)
		return r ^ s
