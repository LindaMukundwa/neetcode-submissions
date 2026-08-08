class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #use a set to keep track of each letter we find in each 
        # add do a 2 pass approach basically 
        # go through each list tracking each letter then compare and return false
        # if they are not the same length, then false
        # assuming uper or lower case does not matter

        # Check lengths first
        if len(s) != len(t):
            return False

        # Compare sorted versions of both strings
        return sorted(s) == sorted(t)
