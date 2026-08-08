class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # take one string and make a hashmap of each letter and occurence
        # pass through second and compare with instances 

        # initilalize hashmap
        myMap = {}

        # knockout question
        if len(s) != len(t):
            return False
        
        # go through first string and add to map
        for char in s:
            if char not in myMap:
                myMap[char]=1
            elif char in myMap:
                myMap[char]+=1

        #  go through second string and compare until not found
        for char in t:
            if char in myMap:
                if myMap[char] == 0:
                    return False
                else:
                    myMap[char]-=1
            else:
                return False
        # if passes completetely then it is True 
        return True
