class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)

        while l<r:
            m=l+((r-l)//2)
            day=1
            capacity=0
            for w in weights:
                
                if capacity+w > m :
                    capacity=0
                    day+=1
                capacity+=w
            if day > days :
                l=m+1
            else:
                r=m
        return r            

        #10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26       
        