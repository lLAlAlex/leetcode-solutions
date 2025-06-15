class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        stack = []
        curr = slow.next
        slow.next = None
        
        while curr:
            stack.append(curr)
            curr = curr.next
        
        curr = head
        
        while stack:
            node = stack.pop()
            next_curr = curr.next
            curr.next = node
            node.next = next_curr
            curr = next_curr