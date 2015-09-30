class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		if not nums:
			return nums
		
		left = 0
		right = 0

		while right < len(nums):
			while right < len(nums) and nums[right] == 0:
				right += 1
			if right == len(nums):
				break
			nums[left] = nums[right]
			left += 1
			right += 1
		while left < len(nums):
			nums[left] = 0
			left += 1
