class Solution:
	# @return a boolean
	def isScramble(self, s1, s2):
		
		def helper(s1, s2, p1, p2, length):

			if length == 0:
				return False
			
			v = [0] * 26
			for i in range(length):
				v[ord(s1[p1 + i]) - ord('a')] += 1
				v[ord(s2[p2 + i]) - ord('a')] -= 1
			for i in v:
				if i != 0:
					return False
			
			if length == 1:
				return True
			
			for i in range(1, length):
				if possible[p1][p2][i] == -1:
					possible[p1][p2][i] = helper(s1, s2, p1, p2, i)
				if possible[p1 + i][p2 + i][length - i] == -1:
					possible[p1 + i][p2 + i][length - i] = helper(s1, s2, p1 + i, p2 + i, length - i)
				if possible[p1][p2][i] and possible[p1 + i][p2 + i][length - i]:
					return True
				if possible[p1][p2 + length - i][i] == -1:
					possible[p1][p2 + length - i][i] = helper(s1, s2, p1, p2 + length - i, i)
				if possible[p1 + i][p2][length - i] == -1:
					possible[p1 + i][p2][length - i] = helper(s1, s2, p1 + i, p2, length - i)
				if possible[p1][p2 + length - i][i] and possible[p1 + i][p2][length - i]:
					return True
			return False
		
		if len(s1) != len(s2):
			return False
		length = len(s1)
		possible = [[[-1] * length for _ in range(length)] for __ in range(length)]
		return helper(s1, s2, 0, 0, length)
