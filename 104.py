# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
def printTree(root: TreeNode):
    if not root:
        return
    
    print(root.val, end="")
    printTree(root.left)
    printTree(root.right)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# printTree(root)

obj = Solution()
print(obj.maxDepth(root))