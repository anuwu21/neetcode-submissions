class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l< r:
            m=l+((r-l)//2)
            day=1
            capacity=0
            for w in weights:
                if capacity + w > m:
                    day+=1
                    capacity = 0
                capacity+=w 

            if day > days:
                l= m +1
            else:
                r=m
        return l        
