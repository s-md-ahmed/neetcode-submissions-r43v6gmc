# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=0
        count=0
        curr=head
        while curr:
            curr=curr.next
            count+=1
        cut=count-n
        if cut==0:
            return head.next
        curr=head
        while curr:
            if i==cut-1:
                curr.next=curr.next.next
                break
            i+=1
            curr=curr.next
        return head