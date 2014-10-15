# Definition for a point
class Point:
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b

class Solution:
	# @param points, a list of Points
	# @return an integer
	def maxPoints(self, points):
		if len(points) <= 1:
			return len(points)
		slopes = {}
		m = 0
		rep = 0
		for i in range(len(points)):
			count = {}
			rep = 0
			for j in range(len(points)):
				if points[i].x == points[j].x and points[i].y == points[j].y:
					rep += 1
					continue
				if i > j:
					if slopes[(j, i)] in count.keys():
						count[slopes[(j, i)]] += 1;
					else:
						count[slopes[(j, i)]] = 1;
				elif i < j:
					if points[i].x == points[j].x:
						slopes[(i, j)] = float('Inf')
					else:
						slopes[(i, j)] = float(points[i].y - points[j].y) / (points[i].x - points[j].x)
					if slopes[(i, j)] in count.keys():
						count[slopes[(i, j)]] += 1;
					else:
						count[slopes[(i, j)]] = 1;
			if m < rep:
				m = rep
			for v in count.itervalues():
				if m < v + rep:
					m = v + rep
		return m

p1 = Point(0, 0)
p2 = Point(1, 1)
p3 = Point(0, 0)
p4 = Point(1, 1)
p5 = Point(1, -1)
s = Solution()
print s.maxPoints([p1, p2, p3, p4, p5])