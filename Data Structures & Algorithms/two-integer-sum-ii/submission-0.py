class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we need to find the complement
        # sort, two pointer/sliding window
        # iterate array, summing up l and r ptr, then increment

        l, r = 0, len(numbers) - 1
        
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                return [l + 1,r + 1]

            elif currSum > target:
                r -=1
            else:
                l+= 1
        return []




