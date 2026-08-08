class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # edge case 
        if len(nums) == 0:
            return 0
        # sort then use a stack for tracking longest
        nums.sort()
        curr_stack = [nums[0]]
        
        # number to store longest subsequence
        longest = 1
        
        for i in range(1, len(nums)):
            # make sure to handle and skip duplicates
            if nums[i] == nums[i-1]:
                continue 
            
            # now check if our number contninues our sequence
            if nums[i] == curr_stack[-1] + 1:
                curr_stack.append(nums[i])
                longest = max(longest, len(curr_stack))
            else:
                # start a new sequence
                curr_stack = [nums[i]] # keep this as a list
        
        return longest