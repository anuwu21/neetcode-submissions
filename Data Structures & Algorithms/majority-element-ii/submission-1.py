class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        d=Counter(nums)
        ans=[]
        for num,c in d.items():
            if c>len(nums)/3:
                ans.append(num)
        return ans        
        