# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        d=ListNode()
        d.next=head
        prev=d

        for i in range(left-1):
            prev=prev.next

        curr=prev.next
        subprev=None
        for i in range(right-left+1):
            temp=curr.next
            curr.next=subprev
            subprev=curr
            curr=temp

        prev.next.next=curr
        prev.next=subprev
        return d.next    

        