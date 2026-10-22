class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        L,R=0,len(nums)-1
        while L<=R:
            M=L+((R-L)//2)
            if nums[M]==target:
                l=M-1
                r=M+1
                while l >= 0 and nums[l] == target:
                    l-=1
                while r<len(nums) and nums[r]==target:
                    r+=1
                return [l+1,r-1]         
            elif nums[M]> target:
                R=M-1
            elif nums[M]<target:
                L=M+1
        return [-1,-1]                        


        