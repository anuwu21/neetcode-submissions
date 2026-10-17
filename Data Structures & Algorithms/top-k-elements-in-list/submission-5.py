class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        new=[]
        d=Counter(nums)
        for i in range(k):        
            new.append(max(d, key=d.get))
            d.pop(max(d, key=d.get))

        print(new)    
        return new    
        
        