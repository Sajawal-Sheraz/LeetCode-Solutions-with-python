#https://leetcode.com/problems/reverse-linked-list/




class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        cur_node = head
        prev = None
        while cur_node is not None:
            next_node = cur_node.next  
            cur_node.next = prev
            prev = cur_node
            cur_node = next_node
        head = prev
        return head
        
