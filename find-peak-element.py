class Solution:
	# @param num, a list of integer
	# @return an integer
	def findPeakElement(self, num):
		
		def find(l, r):
			if r - l < 2:
				if num[l] > num[r]:
					return l
				else:
					return r
			index = (l + r) / 2
			if num[index] > num[index - 1] and num[index] > num[index + 1]:
				return index
			elif num[index - 1] < num[index] and num[index] < num[index + 1]:
				return find(index + 1, r)
			else:
				return find(l, index - 1)
		
		return find(0, len(num) - 1)
