class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # We need a starting point that isn't part of the data
        list3 = ListNode() 
        curr3 = list3 # This is our "pencil" that draws the new list
        
        curr1 = list1
        curr2 = list2
        
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr3.next = curr1    
                curr1 = curr1.next    
            else:
                curr3.next = curr2    
                curr2 = curr2.next     
            
            curr3 = curr3.next         
            
        if curr1:
            curr3.next = curr1

        elif curr2:
            curr3.next = curr2
        return list3.next