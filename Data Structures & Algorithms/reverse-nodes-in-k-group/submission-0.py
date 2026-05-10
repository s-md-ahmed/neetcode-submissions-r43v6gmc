class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 1. Base Case (your idea: "see if u have reached the end")
        if not head:
            return None
        
        # 2. Traverse to k and stop (your idea: "traverse to k and stop there")
        # We check if we actually have k nodes to reverse
        curr = head
        for i in range(k):
            if not curr:
                return head # Not enough nodes? "Close the case" and return as is
            curr = curr.next
        
        # 3. Start reversing (your idea: "start reversing ur nodes")
        prev = None
        current = head
        for _ in range(k):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        # 4. Recursive step (your idea: "constantly keep recalling the function")
        # After reversing, 'head' is now the tail. 
        # It needs to point to the result of the NEXT recursive call.
        head.next = self.reverseKGroup(current, k)
        
        # 'prev' is now the new head of this reversed segment
        return prev