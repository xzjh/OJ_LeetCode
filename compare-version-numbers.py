class Solution:
	# @param version1, a string
	# @param version2, a string
	# @return an integer
	def compareVersion(self, version1, version2):
		s1 = version1.split('.')
		s2 = version2.split('.')
		l = min(len(s1), len(s2))
		for i in range(l):
			if int(s1[i]) < int(s2[i]):
				return -1
			elif int(s1[i]) > int(s2[i]):
				return 1
		if len(s1) < len(s2):
			for i in range(l, len(s2)):
				if int(s2[i]) > 0:
					return -1
		elif len(s1) > len(s2):
			for i in range(l, len(s1)):
				if int(s1[i]) > 0:
					return 1
		
		return 0
