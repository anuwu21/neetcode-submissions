class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=set(nums)
        longest=0

        for n in nums:
            length=0
            if (n-1) not in a:
                while n+length in a:
                    length+=1
                longest=max(longest,length)
        return longest            
                
        