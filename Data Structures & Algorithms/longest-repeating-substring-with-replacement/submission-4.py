class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        d={}
        maxf=0
        length=0
        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r],0)
            maxf=max(maxf,d[s[r]])
            if r-l+1 - maxf > k :
                d[s[l]]-=1
                l+=1
            length=max(length,r-l+1)    
        return length        

        