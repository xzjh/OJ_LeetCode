class Solution:
	# @param A, a list of integers
	# @param target, an integer to be searched
	# @return a list of length 2, [index1, index2]
	def searchRange(self, A, target):
		
		def helper(left, right, target):
			if left <= right:
				mid = (left + right) // 2
				if A[mid] == target:
					l = mid
					r = mid
					while l > left and A[l - 1] == target:
						l -= 1
					while r < right and A[r + 1] == target:
						r += 1
					return [l, r]
				elif A[mid] > target:
					return helper(left, mid - 1, target)
				else:
					return helper(mid + 1, right, target)
			else:
				return [-1, -1]
		
		return helper(0, len(A) - 1, target)
