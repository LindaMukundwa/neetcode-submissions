class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # more optimal solution
        # we are converting nums into a hashset
        # remember hashsets do not allow duplicates
        numSet = set(nums)
        longest = 0
        # iterate through hashset
        for num in numSet:
            # if num - 1 is not in set, it's the starting point
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                    # compare here and then return the highest one
                longest = max(length, longest)
        return longest