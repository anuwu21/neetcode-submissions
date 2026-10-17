class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        d1=Counter(s1)
        l=0
        r=len(s1)-1
        while r<len(s2):
            d2=Counter(s2[l:r+1])
            if d2==d1:
                return True
            l+=1
            r+=1
        return False        