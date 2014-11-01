class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		if not prices:
			return 0
		min_p = prices[0]
		max_profit = 0
		for p in prices:
			if min_p > p:
				min_p = p
			else:
				max_profit = max(max_profit, p - min_p)
		return max_profit