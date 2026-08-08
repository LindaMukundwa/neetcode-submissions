class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # it looks like the list is always sorted
        # creat empty dict to store nums and indices
        seen = {}

        # go through array with both index and value
        for i, num in enumerate(nums):
            # find number needed to find target
            complement = target - num

            if complement in seen:
                # if found in dict, return index of complement and current index
                return [seen[complement], i]
            # if not found, add current number and index to hashmap
            seen[num] = i
        
        # This line should ideally not be reached if a solution is guaranteed to exist
        return []