class Solution:
	# @return a string
	def intToRoman(self, num):
		integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
		roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

		r = ''
		while num > 0:
			for i in range(len(integer)):
				while num >= integer[i]:
					r += roman[i]
					num -= integer[i]
		return r

s = Solution()
print s.intToRoman(3999)