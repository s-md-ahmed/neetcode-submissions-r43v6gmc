class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''curr = head     unoptiized where time and space are big O of N
        list1 = []
        left1 = []
        right1 = []
        
        while curr:
            list1.append(curr.val)
            curr = curr.next
            
        if not list1:
            return

        
        mid = (len(list1) + 1) // 2
        
        
        left1 = list1[:mid]
        right1 = list1[mid:]
        right1.reverse()
        
        
        curr = head
        i = 0
        while curr:
            if i % 2 == 0:
                curr.val = left1.pop(0)
            else:
                curr.val = right1.pop(0)
            
            curr = curr.next
            i += 1    
        print(head)'''
        #actual optimized approach
        #[2,4,6,8]
        if not head or not head.next:
            return

        # --- STEP 1: FIND MIDDLE ---
        # Initial: slow=2, fast=2
        # Loop 1: slow moves to 4, fast moves to 6
        # Loop 2: slow moves to 6, fast moves to None (End)
        # Result: slow is at node 6.
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # --- STEP 2: REVERSE SECOND HALF ---
        # Current: 2 -> 4 -> 6 -> 8
        # prev = None, curr = slow.next (node 8)
        # slow.next = None (List is now: 2 -> 4 -> 6 -> None)
        # Loop 1 (curr is 8):
        #   next_node = None
        #   8.next = None (prev)
        #   prev = 8, curr = None
        # Result: prev is node 8. Second half is just [8].
        prev, curr = None, slow.next
        slow.next = None  
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # --- STEP 3: MERGE --- here  iinitially 2 points to 4 and 4 points to 6 and similarly  right half is 8 points to none 
        # first = 2, second = 8
        # Loop 1:
        #   tmp1 = 2.next (node 4)
        #   tmp2 = 8.next (None)
        #   2.next = 8  (List: 2 -> 8)
        #   8.next = 4  (List: 2 -> 8 -> 4)
        #   first = 4, second = None
        # Loop ends because second is None.
        # Final Result: 2 -> 8 -> 4 -> 6 -> None
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        curr=head
        while curr:
            print(str(curr.val)+"->", end="")
            curr=curr.next
        print("Null",end="")