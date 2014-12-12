# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
	# @param intervals, a list of Intervals
	# @param newInterval, a Interval
	# @return a list of Interval
	def insert(self, intervals, newInterval):
		
		if not intervals:
			return [newInterval]
		
		new_intervals = []
		new_interval = Interval(newInterval.start, newInterval.end)
		for i in range(len(intervals)):
			if new_interval.end < intervals[i].start:
				new_intervals.append(new_interval)
				new_intervals.extend(intervals[i:])
				return new_intervals
			elif new_interval.start > intervals[i].end:
				new_intervals.append(intervals[i])
			else:
				new_interval.start = min(new_interval.start, intervals[i].start)
				new_interval.end = max(new_interval.end, intervals[i].end)
		new_intervals.append(new_interval)
		return new_intervals
