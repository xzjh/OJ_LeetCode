class Solution:
	# @param gas, a list of integers
	# @param cost, a list of integers
	# @return an integer
	def canCompleteCircuit(self, gas, cost):
		if len(gas) == 0:
			return -1
 		net = [x - y for (x, y) in zip(gas, cost)]
 		m = 0
 		s = 0
 		index_temp = 0
 		index = 0
 		le = len(net)
 		for i in range(le * 2):
 			s += net[i % le]
 			if s < 0:
 				s = 0
 				index_temp = i % le + 1
 			if s > m:
 				m = s
 				index = index_temp
 		if s == 0:
 			# all non-positive
 			if net[0] == 0:
 				# all zero
 				return 0
 			else:
 				return -1

 		return index

s = Solution()
a=[1,1]
b=[2,2]
print s.canCompleteCircuit(a,b)