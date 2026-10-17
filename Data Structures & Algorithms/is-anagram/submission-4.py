class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss=list(s)
        tt=list(t)
        for i in s:
            if i in tt:
                ss.remove(i)
                tt.remove(i)
        print(ss)
        print(tt)        
        if ss==[] and tt==[]:
            return True                   
        else:
            return False