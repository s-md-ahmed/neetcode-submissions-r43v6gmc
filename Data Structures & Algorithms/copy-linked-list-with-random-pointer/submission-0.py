class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None: None}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        
        curr = head
        while curr:
            new_node = old_to_new[curr]
            new_node.next = old_to_new[curr.next]
            new_node.random = old_to_new[curr.random]
            curr = curr.next
            
        return old_to_new[head]