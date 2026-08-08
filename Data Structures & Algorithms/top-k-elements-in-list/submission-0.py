class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize the hashmap to keep a list of nums and their occurences
        # go through hashmap and the top 2 elements will be the the final list 
        myMap = {}
        result = []

        for num in nums:
            if num not in myMap:
                myMap[num]=1
            elif num in myMap:
                myMap[num]+=1

        while k != 0:
            topKey = max(myMap, key=myMap.get)
            result.append(topKey)
            myMap.pop(topKey)
            k -= 1
        
        return result
        