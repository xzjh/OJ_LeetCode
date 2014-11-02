class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		if not prices:
			return 0
		max_profit = 0
		length = len(prices)
		l = [0] * length
		r = [0] * length

		min_p = prices[0]
		for i in range(1, length):
			l[i] = max(prices[i] - min_p, l[i - 1])
			min_p = min(min_p, prices[i])

		max_p = prices[length - 1]
		for i in range(0, length - 1)[::-1]:
			r[i] = max(max_p - prices[i], r[i + 1])
			max_p = max(max_p, prices[i])

		for i in range(length):
			max_profit = max(max_profit, l[i] + r[i])
			
		return max_profit

s = Solution()
print s.maxProfit([1,2,4,2,5,7,2,4,9,0])
