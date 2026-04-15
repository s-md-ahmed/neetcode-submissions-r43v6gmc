class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        count = 0
        curr = head

        # 1. Count the nodes
        while curr:
            curr = curr.next
            count += 1
        
        cut = count - n
        curr = head

        # --- THE FIX FOR EXAMPLE 3 ---
        # If cut is 0, it means we are removing the very first node.
        # So we just return the second node (head.next) as the new head.
        if cut == 0:
            return head.next
        # -----------------------------

        # 2. Your original logic for the rest
        while curr:
            if i == cut - 1:
                curr.next = curr.next.next
                break
            i += 1
            curr = curr.next                
        
        return head