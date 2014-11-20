class Solution:
	# @param S, a string
	# @param L, a list of string
	# @return a list of integer
	def findSubstring(self, S, L):
		
		d = {}
		for w in L:
			if w in d:
				d[w] += 1
			else:
				d[w] = 1
		word_length = len(L[0])
		word_num = len(L)
		length = len(S)
		left = 0
		word_left = word_num
		total_words_length = word_num * word_length
		res = []
		for start in range(word_length):
			left = start
			word_left = word_num
			d.clear()
			for w in L:
				if w in d:
					d[w] += 1
				else:
					d[w] = 1
			for i in range(start, length, word_length):
				this_word = str(S[i:i + word_length])
				if this_word in d:
					d[this_word] -= 1
					if d[this_word] >= 0:
						word_left -= 1
					else:
						while d[this_word] < 0:
							first_word = str(S[left:left + word_length])
							d[first_word] += 1
							left += word_length
							if this_word != first_word:
								word_left += 1
					if word_left == 0:
						res.append(left)
						first_word = str(S[left:left + word_length])
						d[first_word] += 1
						left += word_length
						word_left = 1
				else:
					left = i + word_length
					word_left = word_num
					d.clear()
					for w in L:
						if w in d:
							d[w] += 1
						else:
							d[w] = 1
					if left > length - total_words_length:
						break
		return res

s = Solution()
print s.findSubstring("abababab", ["a","b","a"])
