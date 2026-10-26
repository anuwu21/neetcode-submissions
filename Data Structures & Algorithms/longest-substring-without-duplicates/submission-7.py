class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        length=0
        new=set()
        for r in range(len(s)):
            while s[r] in new:
                new.remove(s[l])
                l+=1
            new.add(s[r])
            length=max(length,r-l+1)
        return length        

        