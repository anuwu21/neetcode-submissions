class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        f=0
        res1=True
        res2=True


        while l<r:
            if s[l]!=s[r] and f==0:
                l+=1
                f=1
            elif s[l]!=s[r] and f==1:
                res1 = False
                break
            else:
                l+=1
                r-=1

        l,r=0,len(s)-1
        f=0   

        while l<r:
            if s[l]!=s[r] and f==0:
                r-=1
                f=1
            elif s[l]!=s[r] and f==1:
                res2 = False
                break
            else:
                l+=1
                r-=1

        return res1 or res2       
     



