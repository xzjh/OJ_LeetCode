class Solution:
	# @param s, a string
	# @return a boolean
	def isNumber(self, s):

		s = s.strip()
		if not s:
			return False

		e_flag = False
		e_valid = False
		dot_flag = False
		dot_valid = True
		sign_valid = True

		for c in s:
			if not (c >= '0' and c <= '9'):
				if e_valid and not e_flag and (c == 'e' or c == 'E'):
					e_flag = True
					e_valid = False
					sign_valid = True
				elif dot_valid and not e_flag and not dot_flag and c == '.':
					dot_flag = True
					sign_valid = False
				elif sign_valid and (c == '-' or c == '+'):
					sign_valid = False
				else:
					return False
			else:
				e_valid = True
				sign_valid = False
				dot_valid = True
		return e_valid and dot_valid

s = Solution()
print s.isNumber('.')