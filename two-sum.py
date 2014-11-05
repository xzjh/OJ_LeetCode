class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		sorted_num = sorted(zip(num, range(1, len(num) + 1)))
		index1 = 0
		index2 = len(num) - 1
		while index1 < index2:
			if sorted_num[index1][0] + sorted_num[index2][0] < target:
				index1 += 1
			elif sorted_num[index1][0] + sorted_num[index2][0] > target:
				index2 -= 1
			else:
				return tuple(sorted([sorted_num[index1][1], sorted_num[index2][1]]))
