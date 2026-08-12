class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       # use hashmap to store vals we have seen and their indices
       seen = {}
       for idx, val in enumerate(nums):
            if val in seen and idx - seen[val] <= k:
                return True
            seen[val] = idx  # Always update with the most recent index
       return False