class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs=sorted(strs)

        for i in range(len(strs[0])):
            if i >=len(strs[-1]) or strs[0][i]!=strs[-1][i]:
                return ans
            ans+=strs[0][i] 
        return ans       
        