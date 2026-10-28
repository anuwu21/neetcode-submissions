class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<r:
            m=l+((r-l)//2)
            count=0
            for p in piles:
                count += (p + m - 1) //m   #p/m 
            if count >h:
                count=0
                l=m+1
            else:
                r=m
        return l      


        