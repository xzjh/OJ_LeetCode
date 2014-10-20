class Solution:
	# @param words, a list of strings
	# @param L, an integer
	# @return a list of strings
	def fullJustify(self, words, L):
		
		if not words or not L:
			return ['']

		words_length = 0
		word_num = 0
		i = 0
		ans = []
		while i < len(words):
			word_num = 0
			words_length = 0
			while i < len(words) and words_length + word_num + len(words[i]) <= L:
				# take this word
				words_length += len(words[i])
				word_num += 1
				i += 1
			if word_num == 1:
				ans.append(words[i - 1] + ' ' * (L - words_length))
			elif word_num > 1:
				if i < len(words):
					space_width = (L - words_length) // (word_num - 1)
					extra_space = (L - words_length) % (word_num - 1)
					this_ans = ''
					for j in range(extra_space):
						this_ans += words[i - word_num + j] + ' ' * (space_width + 1)
					this_ans += (' ' * space_width).join(words[i - word_num + extra_space:i])
					ans.append(this_ans)
				else:
					ans.append(' '.join(words[i - word_num:i]) + ' ' * (L - words_length - word_num + 1))
			else:
				return ['']
		return ans

s = Solution()
words=["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."]
print s.fullJustify(words, 30)
