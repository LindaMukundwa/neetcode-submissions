class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we are going to heapify the array
        # then we get max value and right child and subtract difference then 
        # take over as max heap then repear pop process until there is no length left

        # convert every node to negative
        stones = [-num for num in stones] 
        # lets us build an actual min heap
        heapq.heapify(stones)

        while len(stones) > 1:
            # we pop the heaviest stones
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if y > x:
                # if there's a -ve val, push difference into stones
                heapq.heappush(stones, x - y)
        
        stones.append(0)            # so we don't get index error
        return abs(stones[0])       # absolute value of remainder

