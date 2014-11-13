class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        
        def helper(n, k, start, res_item):
            if n < k:
                return
            if k == 0:
                res.append(res_item)
                return
            helper(n - 1, k - 1, start + 1, res_item + [start])
            helper(n - 1, k, start + 1, res_item)
        
        res = []
        helper(n, k, 1, [])
        return res
