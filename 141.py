# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: bool
        """
        hashSet = set()
        
        while head:
            if head in hashSet:
                return True
            hashSet.add(head)
            head = head.next
        
        return False

obj = Solution()
