class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # check it is not empty
        if len(strs) == 0:
            return []
        
        # Use a SortedDict where key is sorted string
        # and value is list of anagrams
        anagram_groups = defaultdict(list)
        # iterate through each strings
        for s in strs:
            # Sort the string to create a key
            # ex. {'bat', 'tab'} is 'abt': 'bat','tab'
            sorted_s = ''.join(sorted(s))
            anagram_groups[sorted_s].append(s)
        
        return list(anagram_groups.values())
         