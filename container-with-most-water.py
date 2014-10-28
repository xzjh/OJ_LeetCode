class Solution:
	# @return an integer
	def maxArea(self, height):
		
		def get_capacity(a, b):
			return min(height[a], height[b]) * (b - a)
		
		if len(height) < 2:
			return 0
		
		a = 0
		b = len(height) - 1
		ans = get_capacity(a, b)
		while b > a:
			if height[a] < height[b]:
				i = a + 1
				while i < b and height[i] <= height[a]:
					i += 1
				a = i
			else:
				i = b - 1
				while i > a and height[i] <= height[b]:
					i -= 1
				b = i
			c = get_capacity(a, b)
			if ans < c:
				ans = c
		return ans