class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        if not height:
            return 0
        stack = []
        height.append(0)
        area = 0
        i = 0
        while i < len(height):
            if not stack or height[i] > height[stack[-1]]:
                stack.append(i)
            else:
                h = stack.pop()
                area = max(area, height[h] * ((i - stack[-1] - 1) if stack else i))
                i -= 1
            i += 1
        return area
