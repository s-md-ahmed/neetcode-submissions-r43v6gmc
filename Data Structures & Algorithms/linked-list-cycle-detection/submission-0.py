class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Start both runners at the beginning
        slow = head
        fast = head
        
        # While the fast runner hasn't hit a dead end
        # We check fast.next to make sure we can move 2 steps
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            # If they land on the exact same node, it's a cycle!
            if slow == fast:
                return True
        
        # If we broke out of the loop, it means fast hit 'None'
        return False