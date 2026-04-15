# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # --- PART 1: EXTRACTION (Your original logic) ---
        arr1 = []
        arr2 = []
        
        curr = l1
        while curr:
            arr1.append(curr.val)
            curr = curr.next
            
        curr = l2
        while curr:
            arr2.append(curr.val)
            curr = curr.next
            
        # --- PART 2: THE MATH (Addition with Carry) ---
        i = 0
        carry = 0
        dummy = ListNode(0)  # The anchor to start our new list
        curr_node = dummy
        
        # We keep going as long as there are digits left in either array OR a carry
        while i < len(arr1) or i < len(arr2) or carry:
            
            # If we run out of digits in arr1, use 0
            if i < len(arr1):
                val1 = arr1[i]
            else:
                val1 = 0
                
            # If we run out of digits in arr2, use 0
            if i < len(arr2):
                val2 = arr2[i]
            else:
                val2 = 0
            
            # Calculate Sum and Carry
            total = val1 + val2 + carry
            carry = total // 10         # Get the tens place (e.g., 1 from 13)
            digit = total % 10          # Get the ones place (e.g., 3 from 13)
            
            # --- PART 3: RECONSTRUCTION ---
            curr_node.next = ListNode(digit) # Create the new link
            curr_node = curr_node.next       # Move the "mover" forward
            i += 1
            
        # Return everything after the dummy node
        return dummy.next