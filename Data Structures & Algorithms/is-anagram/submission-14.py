class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}

        for n in s:
            if n not in d1:
                d1[n]=1
            else:
                d1[n]+=1
        for n in t:
            if n not in d2:
                d2[n]=1
            else:
                d2[n]+=1       
        return d1==d2