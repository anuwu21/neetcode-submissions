class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        new=1
        numset=set(nums)
        while new in numset:
            new+=1
        return new      
        