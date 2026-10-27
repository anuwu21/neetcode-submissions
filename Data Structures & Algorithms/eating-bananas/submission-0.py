class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<r:
            count=0
            m = l + (r - l) // 2
            for p in piles:
                count += (p + m - 1) // m
            if count > h :
                l=m+1
                count=0
            else:
                r=m    

        return l               