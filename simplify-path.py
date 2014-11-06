class Solution:
	# @param path, a string
	# @return a string
	def simplifyPath(self, path):
		ds = path.strip('/').split('/')
		for i in range(1, len(ds))[::-1]:
			if ds[i] == '':
				del ds[i]
		stack = []
		for d in ds:
			if d == '.':
				continue
			elif d == '..':
				if stack:
					stack.pop()
			else:
				stack.append(d)
		return '/' + '/'.join(stack)
