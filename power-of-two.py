class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        s = 1
        while s < n:
            s *= 2
        if s == n:
            return True
        else:
            return False