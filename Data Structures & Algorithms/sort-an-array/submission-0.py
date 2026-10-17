class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        for k in range(len(nums)-1):
            for i in range(1,len(nums)):
                if nums[i]<nums[i-1]:
                    nums[i],nums[i-1]=nums[i-1],nums[i]
        return nums                  