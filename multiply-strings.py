class Solution:
	# @param num1, a string
	# @param num2, a string
	# @return a string
	def multiply(self, num1, num2):
		
		n1 = map(int, num1)
		n2 = map(int, num2)
		length_n1 = len(n1)
		length_n2 = len(n2)
		length = length_n1 + length_n2
		res = [0] * length
		times_carry = 0
		add_carry = 0
		
		for j in range(length_n2)[::-1]:
			for i in range(length_n1)[::-1]:
				times_res = n1[i] * n2[j] + times_carry
				times_carry = times_res // 10
				add_res = res[i + j + 1] + times_res % 10 + add_carry
				res[i + j + 1] = add_res % 10
				add_carry = add_res // 10
			res[j] += times_carry + add_carry
			times_carry = 0
			add_carry = 0
			
		i = 0
		while i < length - 1 and res[i] == 0:
			i += 1
		return ''.join(map(str, res[i:]))
