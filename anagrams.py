class Solution:
	# @param strs, a list of strings
	# @return a list of strings
	def anagrams(self, strs):

		def get_key(word):
			return ''.join(sorted(word))

		if strs == None or len(strs) == 0:
			return None

		groups = {}
		for word in strs:
			key = get_key(word)
			if groups.has_key(key):
				groups[key].append(word)
			else:
				groups[key] = [word]

		ana = []
		for words in groups.itervalues():
			if len(words) > 1:
				ana.extend(words)

		return ana

s = Solution()
l = ['a', 'bc', 'cb', 'd', 'a']
print s.anagrams(l)