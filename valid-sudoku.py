class Solution:
	# @param board, a 9x9 2D array
	# @return a boolean
	def isValidSudoku(self, board):
		for i in range(9):
			d = {}
			row = board[i]
			for n in row:
				if n != '.':
					if n in d:
						return False
					else:
						d[n] = 1
		for j in range(9):
			d = {}
			for i in range(9):
				if board[i][j] != '.':
					if board[i][j] in d:
						return False
					else:
						d[board[i][j]] = 1
		for i in range(9)[::3]:
			for j in range(9)[::3]:
				d = {}
				for a in range(3):
					for b in range(3):
						if board[i + a][j + b] != '.':
							if board[i + a][j + b] in d:
								return False
							else:
								d[board[i + a][j + b]] = 1
								
		return True
