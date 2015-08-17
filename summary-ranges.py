class Solution:
	# @param {integer[]} nums
	# @return {string[]}
	def summaryRanges(self, nums):
		if not nums:
			return []
		if len(nums) == 1:
			return [str(nums[0])]
		start = nums[0]
		end = nums[0]
		res = []
		for i in range(1, len(nums)):
			if nums[i] - 1 != nums[i - 1]:
				if start == end:
					res.append(str(start))
				else:
					res.append(str(start) + '->' + str(end))
				start = nums[i]
			end = nums[i]
		
		if start == end:
			res.append(str(start))
		else:
			res.append(str(start) + '->' + str(end))

		return res
