class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}

        for i in range(len(nums)):
            a=target-nums[i]

            if a in d:
                return [d[a],i]

            d[nums[i]]=i




            





        