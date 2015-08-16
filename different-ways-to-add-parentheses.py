class Solution:
	# @param {string} input
	# @return {integer[]}
	def diffWaysToCompute(self, input):
		
		def helper(nums, ops):
			if len(nums) == 1:
				return nums
			res = []
			for i in range(1, len(nums)):
				nums_left = nums[:i]
				nums_right = nums[i:]
				op = ops[i - 1]
				ops_left = ops[:i - 1]
				ops_right = ops[i:]
				res_left = helper(nums_left, ops_left)
				res_right = helper(nums_right, ops_right)
				for re_left in res_left:
					for re_right in res_right:
						if op == '+':
							res.append(re_left + re_right)
						elif op == '-':
							res.append(re_left - re_right)
						else:
							res.append(re_left * re_right)
			return res
		
		num = 0
		nums = []
		ops = []
		for c in input:
			if c >= '0' and c <= '9':
				num = num * 10 + int(c)
			else:
				ops.append(c)
				nums.append(num)
				num = 0
		nums.append(num)
		return helper(nums, ops)

s = Solution()
print s.diffWaysToCompute('1+2+3')
