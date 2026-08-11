class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        while head and head.val == val:
            head = head.next

        if not head:
            return None
            
        curr = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                # ONLY move forward if we didn't delete
                curr = curr.next
                
        return head