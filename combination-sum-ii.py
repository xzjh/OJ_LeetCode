class Solution:
	# @param candidates, a list of integers
	# @param target, integer
	# @return a list of lists of integers
	def combinationSum2(self, candidates, target):
		
		def iter(candidates, target, ans, sol):

			if target == 0:
				sol.append(ans)
				return

			if len(candidates) == 0:
				return

			candidate = candidates[0]
			if target < candidate:
				return
			else:
				iter(candidates[1:], target - candidate, ans + [candidate], sol)
				i = 0
				while i < len(candidates) - 1 and candidates[i + 1] == candidates[i]:
					i += 1
				# will not select this candidate, remove all this value
				iter(candidates[i + 1:], target, ans, sol)
		sol = []
		iter(sorted(candidates), target, [], sol)
		return sol

s = Solution()
print s.combinationSum2([1,1],2)