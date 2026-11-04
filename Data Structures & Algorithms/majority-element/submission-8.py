class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        res=0
        MaxCount=0

        for n in nums:
            count[n]= 1 + count.get(n,0)
            if count[n]>MaxCount:
                res=n
            MaxCount = max(count[n],MaxCount)
        return res    

        