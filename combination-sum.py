class Solution:
	# @param candidates, a list of integers
	# @param target, integer
	# @return a list of lists of integers
	def combinationSum(self, candidates, target):
		
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
				iter(candidates[1:], target, ans, sol)
				iter(candidates, target - candidate, ans + [candidate], sol)

		sol = []
		iter(sorted(candidates), target, [], sol)
		return sol

s = Solution()
print s.combinationSum([2,3,6,7],7)