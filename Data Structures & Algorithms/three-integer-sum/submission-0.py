class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # o(n^2) time complexity to sort which is logn then nested loop
        # o(n) space for result
        # Sort the array first, very important for the two-pointer approach
        nums.sort()
        result = [] # storing the resulting triplets
        
        # Iterate through the array, fixing the first element
        for i in range(len(nums) - 2): #Leave room for left and right pointer
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # Two pointers: left starts right after i, right starts at the end
            left, right = i + 1, len(nums) - 1
            
            # Loop to make them move until they meet in the middle
            while left < right:
                total = nums[i] + nums[left] + nums[right] # keep track of the target outside ifs
                
                if total == 0:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers and skip duplicates
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # Skip duplicate values for right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif total < 0:
                    # Sum is too small, move left pointer to increase sum
                    left += 1
                else:
                    # Sum is too large, move right pointer to decrease sum
                    right -= 1
        
        return result