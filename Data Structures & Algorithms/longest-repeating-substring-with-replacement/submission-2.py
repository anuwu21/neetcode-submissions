class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l=0
        length=0
        for r in range(len(s)):
            d[s[r]]=1 + d.get(s[r],0)
            while r-l+1  - max(d.values()) > k:
                d[s[l]] -= 1
                l+=1
            length=max(length,r-l+1)
        return length    

        