class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        numset=set(nums)

        new=1

        while new in numset:
            new+=1
        return new    