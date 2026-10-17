class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest=-1
        
        i=len(arr)-1
        while i>=0:
            current=arr[i]
            arr[i]=greatest
            i-=1


            if current > greatest:
                greatest=current

        return arr       
        