class Solution:
	# @param num, a list of integer
	# @return a list of lists of integers
	def permuteUnique(self, num):
		
		def iter(item, num):
			if not num:
				res.append(item)
				return
				
			iter(item + [num[0]], num[1:])
			if len(num) > 1:
				i = 1
				while i < len(num):
					if num[i] != num[i - 1]:
						iter(item + [num[i]], num[:i] + num[i + 1:])
					i += 1
		
		res = []
		iter([], sorted(num))
		return res
