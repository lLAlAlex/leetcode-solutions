# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def insert(self, val):
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # res = int(num1[::-1]) + int(num2[::-1])
        # resStr = str(res)[::-1]
        
        # node = ListNode()
        
        # for c in resStr:
        #     node.val = int(c)
            
        #     if node.next is None:
        #         node.next = ListNode()
                
        #     node = node.next
        
        # return node
        print(n1)
        print(n2)

obj = Solution()
n1 = ListNode()
n1.insert(3)
n1.insert(4)
n1.insert(2)

n2 = ListNode()
n2.insert(4)
n2.insert(6)
n2.insert(5)
print(obj.addTwoNumbers(n1, n2))