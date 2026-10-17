class Solution:
    def validPalindrome(self, s: str) -> bool:
        f,l=0,len(s)-1
        while f<l:
            if s[f]!=s[l]:
                return self.check(s,f+1,l) or self.check(s,f,l-1)
              
            f+=1
            l-=1
        return True
                


    def check(self,s,f,l):
        while f<l:
            if s[f]!=s[l]:
                return False
            else:
                f+=1
                l-=1
        return True        

           