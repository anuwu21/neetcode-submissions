class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    

        d=Counter(nums)

        return max(d,key=d.get)            
        