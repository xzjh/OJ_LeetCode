class Solution:
	# @param board, a list of lists of 1 length string
	# @param word, a string
	# @return a boolean
	def exist(self, board, word):

		def helper(board, word, i, j, m, n):
			if word == '':
				return True
			coords = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
			for coord in coords:
				if coord[0] >= 0 and coord[0] < m and coord[1] >= 0 and coord[1] < n and board[coord[0]][coord[1]] == word[0]:
					board[coord[0]][coord[1]] = '*'
					ret = helper(board, word[1:], coord[0], coord[1], m, n)
					board[coord[0]][coord[1]] = word[0]
					if ret:
						return ret
			return False

		m = len(board)
		n = len(board[0])
		b = map(list, board)
		for i in range(m):
			for j in range(n):
				if b[i][j] == word[0]:
					b[i][j] = '*'
					ret = helper(b, word[1:], i, j, m, n)
					b[i][j] = word[0]
					if ret:
						return ret
		return False

s = Solution()
board = ["ABCE","SFCS","ADEE"]
print s.exist(board, 'ABCB')
