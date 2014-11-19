class Solution:
	# @param A a list of integers
	# @param target an integer
	# @return a boolean
	def search(self, A, target):
		
		start = 0
		end = len(A) - 1
		while start <= end:
			mid = (start + end) // 2
			if A[mid] == target:
				return True
			if A[mid] > A[start]:
				if target >= A[start] and target < A[mid]:
					end = mid - 1
				else:
					start = mid + 1
			elif A[mid] < A[start]:
				if target > A[mid] and target <= A[end]:
					start = mid + 1
				else:
					end = mid - 1
			else:
				start += 1
		
		return False
