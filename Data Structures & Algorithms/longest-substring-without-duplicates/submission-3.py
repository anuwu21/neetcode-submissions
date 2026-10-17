class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        output=0
        res = set()

        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l+=1
            res.add(s[r])    

            output = max(output,r-l+1)
        return output    
        
        