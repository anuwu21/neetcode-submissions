class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        length=0
        window=set()
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            if s[r] not in window:
                window.add(s[r])
            r+=1
            length=max(length,r-l)
        return length    
        