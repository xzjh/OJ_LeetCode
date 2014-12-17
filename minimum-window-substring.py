class Solution:
	# @return a string
	def minWindow(self, S, T):
		
		def is_ok(d, d2):
			for (k, v) in d2.iteritems():
				if not (k in d and d[k] >= v):
					return False
			return True
		
		if not S or not T:
			return ''
		
		d = {}
		d2 = {}
		left = 0
		right = 0
		min_len = len(S) + 1
		min_str = ''
		for c in T:
			if c in d2:
				d2[c] += 1
			else:
				d2[c] = 1
		while right < len(S):
			if S[right] in d:
				d[S[right]] += 1
			else:
				d[S[right]] = 1
			right += 1
			while is_ok(d, d2):
				if min_len > right - left:
					min_len = right - left
					min_str = S[left:right]
				d[S[left]] -= 1
				left += 1
		return min_str
