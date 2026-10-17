class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        ans=""
        for c in nums:
            
            if count==0 :
                ans=c
                count+=1
            elif c!=ans:
                count-=1    
            elif count>0 and c==ans:
                count+=1    
        return ans       
                
                

        
        