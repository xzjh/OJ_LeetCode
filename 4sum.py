class Solution:
	# @return a list of lists of length 4, [[val1,val2,val3,val4]]
	def fourSum(self, num, target):

		sorted_num = sorted(num)
		length = len(sorted_num)
		two_sums = {}
		res = set([])
		for i in range(length):
			for j in range(i + 1, length):
				s = sorted_num[i] + sorted_num[j]
				if s in two_sums:
					two_sums[s].append((i, j))
				else:
					two_sums[s] = [(i, j)]

		for s1, indexes1 in two_sums.iteritems():
			s2 = target - s1
			if s2 in two_sums:
				indexes2 = two_sums[s2]
				for index1 in indexes1:
					for index2 in indexes2:
						if index1[0] != index2[0] and \
							index1[1] != index2[0] and \
							index1[0] != index2[1] and \
							index1[1] != index2[1]:
							res.add(tuple(sorted([ \
								sorted_num[index1[0]], \
								sorted_num[index1[1]], \
								sorted_num[index2[0]], \
								sorted_num[index2[1]]])))
		return map(list, res)


s = Solution()
print s.fourSum([-3,-1,0,2,4,5],0)

