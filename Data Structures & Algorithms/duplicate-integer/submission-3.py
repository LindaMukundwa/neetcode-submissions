class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a set to check if we have seen the value
        # iterate through nums, check value and if in set, end, if not, continue

        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False