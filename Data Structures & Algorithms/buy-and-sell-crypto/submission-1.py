class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # subtract from end, sell - buy > 0
        # we will use a sliding window and decreases from the left
        # compare left item with rightmost then go down from maxium profit
        # stop right before element 
        # repeat till we get the end and see if largest num exists
    
        left, right = 0, 1 # two pointerss      
        highest = 0

        while right < len(prices): 
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                highest = max(profit, highest)
            else:
                left = right # point in which we swap because no profit
            right += 1 # move window

        return highest