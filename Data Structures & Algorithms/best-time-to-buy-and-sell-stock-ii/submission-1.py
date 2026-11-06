class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r=1
        l=0
        profit=0
        while r<len(prices):
            if prices[r]>prices[l]:
                profit+=prices[r]-prices[l]
            l=r
            r=r+1
        return profit            

        
        