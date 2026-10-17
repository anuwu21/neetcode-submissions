class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        curr=0

        while curr<len(arr):
            replace=0
            for i in range(curr+1,len(arr)):
                
                if arr[i]>replace:
                    replace=arr[i]
            arr[curr]=replace
            curr+=1
            replace=0

        arr[-1]=-1

        return arr


        