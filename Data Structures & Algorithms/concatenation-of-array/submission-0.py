class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # get one pass solution where we double size of input arr
        n = len(nums)
        ans = [0] * (2 * n)

        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num # from problem statement
        return ans 