class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            b=target-nums[i]
            if b in d:
                return [d[b],i]
            else:
                d[nums[i]]=i    


        