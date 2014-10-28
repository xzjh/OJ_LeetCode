class Solution:
	# @param board, a 9x9 2D array
	# Solve the Sudoku by modifying the input board in-place.
	# Do not return any value.
	def solveSudoku(self, board):

		def is_valid(board, i, j):
			for k in range(9):
				if k != i and board[k][j] == board[i][j]:
					return False
			for k in range(9):
				if k != j and board[i][k] == board[i][j]:
					return False
			for k in range(i // 3 * 3, i // 3 * 3 + 3):
				for h in range(j // 3 * 3, j // 3 * 3 + 3):
					if k != i and j != h and board[k][h] == board[i][j]:
						return False
			return True
		
		def iter(board, i, j):
			if j >= 9:
				return iter(board, i + 1, 0)
			if i == 9:
				return True

			if board[i][j] == '.':
				for k in range(1, 10):
					board[i][j] = str(k)
					if is_valid(board, i, j):
						if iter(board, i, j + 1):
							return True
					board[i][j] = '.'
			else:
				return iter(board, i, j + 1)
			return False

		b = map(list, board)
		iter(b, 0, 0)
		for i in range(len(board)):
			board[i] = ''.join(b[i])

s = Solution()
b = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
s.solveSudoku(b)
print b