class Solution:
	# @param start, a string
	# @param end, a string
	# @param dict, a set of string
	# @return a list of lists of string
	def findLadders(self, start, end, dict):
		
		def get_adjacent(node):
			l = set([])
			for i in xrange(len(node)):
				for c in 'abcdefghijklmnopqrstuvwxyz':
					if node[i] == c:
						continue
					new_word = node[:i] + c + node[i + 1:]
					if new_word in dict:
						l.add(new_word)

			return l

		def get_paths(cur_path, paths):

			last_node = cur_path[-1]

			ret = []
			next_nodes = paths[last_node]
			if len(next_nodes) == 0:
				return [[last_node]]
			for next_node in next_nodes:
				next_paths = get_paths(cur_path + [next_node], paths)
				for path in next_paths:
					ret.append([last_node] + path)
			return ret

		dict.add(start)
		dict.add(end)

		graph = {}
		dist_s = {}
		dist_e = {}
		for word in dict:
			# graph[word] = get_adjacent(word)
			dist_s[word] = 100000
			dist_e[word] = 100000

		qs = set([start])
		qe = set([end])
		qsn = set([])
		qen = set([])
		intersection = set([])
		dist_s[start] = 0
		dist_e[end] = 0
		graph[start] = get_adjacent(start)
		graph[end] = get_adjacent(end)
		paths = {start: []}
		pathe = {end: []}
		while len(qs) > 0 and len(qe) > 0:

			while len(qs) > 0:
				node = qs.pop()
				for child in graph[node]:
					if dist_s[node] + 1 < dist_s[child]:
						dist_s[child] = dist_s[node] + 1
						qsn.add(child)
						paths[child] = [node]
						if child not in graph:
							graph[child] = get_adjacent(child)
					elif dist_s[node] + 1 == dist_s[child]:
						# more than one path to this node
						paths[child].append(node)

			intersection = qsn & qe
			if len(intersection) > 0:
				break

			while len(qe) > 0:
				node = qe.pop()
				for child in graph[node]:
					if dist_e[node] + 1 < dist_e[child]:
						dist_e[child] = dist_e[node] + 1
						qen.add(child)
						pathe[child] = [node]
						if child not in graph:
							graph[child] = get_adjacent(child)
					elif dist_e[node] + 1 == dist_e[child]:
						# more than one path to this node
						pathe[child].append(node)

			intersection = qsn & qen
			if len(intersection) > 0:
				break

			qs = qsn
			qe = qen
			qsn = set([])
			qen = set([])

		if len(intersection) > 0:
			# ans = []
			# for common_node in intersection:
			# 	p = [common_node]
			# 	node = common_node
			# 	while node != start:
			# 		node = paths[node]
			# 		p.append(node)
			# 	p.reverse()
			# 	node = common_node
			# 	while node != end:
			# 		node = pathe[node]
			# 		p.append(node)
			# 	ans.append(p)
			# return ans
			ans = []
			for common_node in intersection:
				pss = get_paths([common_node], paths)
				for ps in pss:
					ps.reverse()
				pes = get_paths([common_node], pathe)
				for ps in pss:
					for pe in pes:
						ans.append(ps + pe[1:])
			return ans
		else:
			return []

s = Solution()
start = "red"
end = "tax"
dict = ["ted","tex","red","tax","tad","den","rex","pee"]
print s.findLadders(start,end,set(dict))