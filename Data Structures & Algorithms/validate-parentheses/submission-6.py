class Solution:
    def isValid(self, s: str) -> bool:

        hashm={")":"(","}":"{","]":"["}

        ans=[]
        for c in s:
            if c in hashm:
                if c in hashm and ans and ans[-1]==hashm[c]:
                    ans.pop(-1)
                else:
                    return False    
            else:
                ans.append(c)
        return len(ans)==0