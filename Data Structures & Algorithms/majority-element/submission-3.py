class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0

        for c in nums:
            
            if count==0 :
                ans=c
                count+=1
            elif c!=ans:
                count-=1    
            else:
                count+=1    
        return ans       
                
                

        
        