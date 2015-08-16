class Solution:
	# @param {integer} num
	# @return {integer}
	def addDigits(self, num):
		
		def helper(num):
			num_str = str(num)
			if len(num_str) == 1:
				return num
			else:
				s = 0
				for d in num_str:
					s += int(d)
				return helper(s)
		
		return helper(num)
