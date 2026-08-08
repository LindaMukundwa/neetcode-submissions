class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # iterate through entire array
        # two pointers for left and right, get sum and compare max
        # return that at the end

        l, result, r = 0, 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            result = max(result, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return result