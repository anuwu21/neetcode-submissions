class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
    
        new=1        
        while True:
            if new not in nums:
                return new
            new=new+1