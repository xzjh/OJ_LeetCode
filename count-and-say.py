class Solution:
	# @return a string
	def countAndSay(self, n):
		if n == 1:
			return '1'
			
		s = '1*'
		for i in range(n - 1):
			count = 0
			last_c = s[0]
			res = ''
			for c in s:
				if c != last_c:
					res += str(count) + last_c
					count = 0
				last_c = c
				count += 1
			s = res + '*'
		return res

s = Solution()
print s.countAndSay(10)
