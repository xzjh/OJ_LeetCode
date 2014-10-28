class Solution:
	# @return an integer
	def atoi(self, str):
		
		st = str.strip()
		if not st:
			return 0
		sign = 1
		if st[0] == '-':
			sign = -1
			st = st[1:]
		elif st[0] == '+':
			st = st[1:]
		dot_flag = False
		ss = ''
		for c in st:
			if c >= '0' and c <= '9':
				ss += c
			elif not dot_flag and c == '.':
				ss += c
				dot_flag = True
			else:
				break
		res = 0
		if ss:
			res = sign * int(ss)
		if res > 2147483647:
			res = 2147483647
		elif res < -2147483648:
			res = -2147483648
		return res

s = Solution()
print s.atoi('-1')