class Solution:
    def calPoints(self, operations: List[str]) -> int:

        ans=[]
        for c in operations:
            if c=="+":
                value=0
                value+=ans[-1] + ans[-2]
                ans.append(value)
            elif c=="C":
                ans.pop(-1)
            elif c=="D":
                mul=ans[-1]*2
                ans.append(mul)
            else:
                ans.append(int(c))       

        total=0 
        for n in ans:
            total+=int(n)   

        return total                     
        