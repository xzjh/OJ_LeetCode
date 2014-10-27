class Solution:
	# @param s, a string
	# @return an integer
	def longestValidParentheses(self, s):
		length = len(s)
		dp = [0] * length
		ma = 0
		for i in range(1, length):
			if s[i] == '(':
				dp[i] = 0
			else:
				if s[i - 1] == '(':
					if i - 2 >= 0 and dp[i - 2] > 0:
						dp[i] = dp[i - 2] + 2
					else:
						dp[i] = 2
				else:
					if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
						dp[i] = dp[i - 1] + 2
						if i - dp[i - 1] - 2 >= 0 and dp[i - dp[i - 1] - 2] > 0:
							dp[i] += dp[i - dp[i - 1] - 2]
				if dp[i] > ma:
					ma = dp[i]
		return ma

s = Solution()
print s.longestValidParentheses("(()())")