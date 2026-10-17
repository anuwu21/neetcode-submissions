class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        a=set(nums)
        longest=0

        for num in nums:
            length=0
            if num-1 not in a:
                while (num+length) in a:
                    length+=1
                longest=max(longest,length)
        return longest            
                
        