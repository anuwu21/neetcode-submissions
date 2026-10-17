class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=prices[0]
        
        new=0

        for i in range(len(prices)):
            if prices[i]<=minn:
                minn=prices[i]
                
            else:
                b=prices[i]-minn
                if b>new:
                    new=b
        return new        
