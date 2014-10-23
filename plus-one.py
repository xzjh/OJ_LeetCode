class Solution:
	# @param digits, a list of integer digits
	# @return a list of integer digits
	def plusOne(self, digits):
		digits.append(0)
		for i in range(len(digits) - 1)[::-1]:
			digits[i + 1] = digits[i]
		digits[0] = 0
		carry = 0
		for i in range(len(digits))[::-1]:
			digits[i] += 1 + carry
			if digits[i] >= 10:
				carry = 0
				digits[i] -= 10
			else:
				carry = -1
		if digits[0] == 0:
			for i in range(len(digits) - 1):
				digits[i] = digits[i + 1]
			digits.pop()
		return digits

s = Solution()
print s.plusOne([1,0])