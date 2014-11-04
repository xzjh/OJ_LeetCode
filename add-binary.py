class Solution:
	# @param a, a string
	# @param b, a string
	# @return a string
	def addBinary(self, a, b):
		if len(b) > len(a):
			a, b = b, a
		carry = False
		res = []
		offset = len(a) - len(b)
		b = '0' * offset + b
		for i in range(len(b))[::-1]:
			if b[i] == '1' and a[i] == '1':
				if carry:
					res.append('1')
				else:
					res.append('0')
				carry = True
			elif b[i] == '1' and a[i] == '0' or b[i] == '0' and a[i] == '1':
				if carry:
					res.append('0')
				else:
					res.append('1')
			else:
				if carry:
					res.append('1')
				else:
					res.append('0')
				carry = False
		if carry:
			res.append('1')
		res.reverse()
		return ''.join(res)
