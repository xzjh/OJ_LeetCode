class Solution:
	# @param board, a 2D array
	# Capture all regions by modifying the input board in-place.
	# Do not return any value.
	def BFS(self, board, start_point, (h, w)):
		q = [start_point]
		while len(q) > 0:
			p = q.pop(0)
			board[p[0]][p[1]] = 'Y'
			if p[1] - 1 >= 0 and board[p[0]][p[1] - 1] == 'O':
				q.append((p[0], p[1] - 1))

			if p[1] + 1 < w and board[p[0]][p[1] + 1] == 'O':
				q.append((p[0], p[1] + 1))

			if p[0] - 1 >= 0 and board[p[0] - 1][p[1]] == 'O':
				q.append((p[0] - 1, p[1]))

			if p[0] + 1 < h and board[p[0] + 1][p[1]] == 'O':
				q.append((p[0] + 1, p[1]))

	def solve(self, board):
		def rep(char):
			if char == 'Y':
				return 'O'
			elif char == 'O':
				return 'X'
			else:
				return char

		if board == None or len(board) == 0:
			return board

		h, w = len(board), len(board[0])
		for i in range(w):
			if board[0][i] == 'O':
				self.BFS(board, (0, i), (h, w))
			if board[h - 1][i] == 'O':
				self.BFS(board, (h - 1, i), (h, w))

		for i in range(h):
			if board[i][0] == 'O':
				self.BFS(board, (i, 0), (h, w))
			if board[i][w - 1] == 'O':
				self.BFS(board, (i, w - 1), (h, w))
				
		board = map(lambda x: map(rep, x), board)
		return board

s = Solution()
b = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
print s.solve(b)
