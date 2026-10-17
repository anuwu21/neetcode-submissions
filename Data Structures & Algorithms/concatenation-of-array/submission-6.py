class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        new=[]
        for n in range(2):
            for i in nums:
                new.append(i)
        return new    
        