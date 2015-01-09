class Solution:
	# @param num, a list of integers
	# @return an integer
	def majorityElement(self, num):
		maj_index = 0
		count = 1
		for i in range(1, len(num)):
			if num[i] == num[maj_index]:
				count += 1
			else:
				count -= 1
			if count == 0:
				maj_index = i
				count = 1
		return num[maj_index]
