class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currprof=0
        l=0
        r=1

        while r<len(prices):
            if prices[l]<prices[r]:
                new = prices[r]-prices[l]
                currprof=max(currprof,new)
            elif prices[l]>prices[r]:
                l=r
            r+=1
        return currprof        
