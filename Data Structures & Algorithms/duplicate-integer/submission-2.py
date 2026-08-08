class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create an empty hash set (set in Python)

        for num in nums:  # Iterate through each number in the input list
            if num in seen:  # Check if the current number is already in the set
                return True  # If it is, a duplicate is found, return True immediately
            seen.add(num)  # If not, add the number to the set

        return False  # If the loop finishes without finding duplicates, return False
