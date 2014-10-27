# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
	# @param intervals, a list of Interval
	# @return a list of Interval
	def merge(self, intervals):
		intervals = sorted(intervals, key = lambda x: x.start)
		i = 1
		while i < len(intervals):
			if intervals[i].start <= intervals[i - 1].end:
				intervals[i - 1].end = max(intervals[i - 1].end, intervals[i].end)
				del intervals[i]
			else:
				i += 1
		return intervals
