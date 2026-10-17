class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        

        # [3,2,2,3] --> nums[:len(a)] --> nums[:2]

        f,s=0,0

        while f < len(nums) :
            if nums[f] != val:
                nums[f],nums[s]= nums[s],nums[f]
                s+=1
            f+=1
        return s                