class Solution:
	# @return a boolean
	def isPalindrome(self, x):
		if x < 0:
			return False
		digits_num = 0
		t = x
		while t != 0:
			t //= 10
			digits_num += 1
		for i in range(digits_num / 2):
			if x // (10 ** (digits_num - 1 - i)) % 10 != x // (10 ** i) % 10:
				return False
		return True

s = Solution()
print s.isPalindrome(0110)