class Solution:
	# @return an integer
	def threeSumClosest(self, num, target):
		
		min_v = 100000
		res = 0
		num = sorted(num)
		
		i = 0
		while i < len(num):
			start = i + 1
			end = len(num) - 1
			while start < end:
				s = num[i] + num[start] + num[end]
				if s == target:
					return target
				elif s < target:
					if min_v > target - s:
						min_v = target - s
						res = s
					start += 1
				else:
					if min_v > s - target:
						min_v = s - target
						res = s
					end -= 1
			i += 1
			if i + 1 < len(num) and num[i] == num[i - 1]:
				i += 1
		return res
