class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		if not citations:
			return 0
		left = 0
		right = len(citations) - 1
		while left <= right:
			mid = (left + right) // 2
			if citations[mid] >= len(citations) - mid:
				right = mid - 1
			else:
				left = mid + 1
		return len(citations) - mid if citations[mid] >= len(citations) - mid else len(citations) - mid - 1
