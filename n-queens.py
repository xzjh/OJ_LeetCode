class Solution:
	# @return a list of lists of string
	def solveNQueens(self, n):
		
		def check(board, n):
			if not board:
				return True
			i_this_row = len(board)
			for i in range(i_this_row):
				j = board[i]
				if j == n:
					return False
				elif abs(j - n) == i_this_row - i:
					return False
			return True
			
		def iter(board):
			nrow = len(board)
			if nrow == n:
				res.append(board)
				return
			for j in range(n):
				if check(board, j):
					iter(board + [j])
			
		if n <= 0:
			return None
		res = []
		iter([])
		output = []
		for this_board in res:
			output_board = []
			for j in this_board:
				output_row = '.' * j + 'Q' + '.' * (n - j - 1)
				output_board.append(output_row)
			output.append(output_board)
		return output

s = Solution()
print s.solveNQueens(4)
