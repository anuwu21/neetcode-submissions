class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        res=0
        MaxCount=0

        for n in nums:
            count[n]= 1 + count.get(n,0)

            res= n if count[n] > MaxCount else res
            MaxCount = max(count[n],MaxCount)
        return res    

        