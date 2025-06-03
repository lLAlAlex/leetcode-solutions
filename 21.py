# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insert(self, ls):
        temp = ListNode()
        curr = temp
        
        for x in ls:
            curr.next = ListNode(x)
            curr = curr.next
        
        return temp.next
        
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = ListNode()
        curr = temp
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 or list2
        
        return temp.next

def printNode(node: ListNode):
    while node:
        print(node.val)
        node = node.next

obj = Solution()
node1, node2 = obj.insert([1,2,4]), obj.insert([1,3,4])

# printNode(node1)
# printNode(node2)

printNode(obj.mergeTwoLists(node1, node2))