class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
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
        print(head)