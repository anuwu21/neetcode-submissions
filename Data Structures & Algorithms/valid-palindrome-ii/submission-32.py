class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r,f=0,len(s)-1,0
        res1,res2=True,True

        while l<r:
            if s[l]!=s[r] and f==0:
                l+=1
                f=1
            elif s[l]!=s[r]:
                res1=False
                break
            else:
                l+=1
                r-=1

        l,r,f=0,len(s)-1,0

        while l<r:  
            if s[l]!=s[r] and f==0:
                r-=1
                f=1
            elif s[l]!=s[r]:
                res2=False
                break
            else:
                l+=1
                r-=1 

        return res1 or res2                     

        