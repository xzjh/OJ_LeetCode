class Solution:
	
	def __init__(self):
		self.res = 0
	# @return an integer
	def totalNQueens(self, n):
		
		
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
				self.res += 1
				return
			for j in range(n):
				if check(board, j):
					iter(board + [j])
			
		if n <= 0:
			return None
		iter([])
		return self.res

s = Solution()
print s.totalNQueens(4)