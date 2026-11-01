# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        if not head or not head.next or not head.next.next:
            return 

        f,s=head,head    

        while f and f.next:
            s=s.next
            f=f.next.next

        curr=s.next
        s.next=None
        prev=None
    
        
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        front=head
        back = prev

        
        while back:
              front_temp=front.next
              back_temp=back.next
              front.next=back
              back.next=front_temp

              front=front_temp
              back=back_temp