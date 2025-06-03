# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def printTree(self, root: TreeNode):
        if not root:
            return
        self.printTree(root.left)
        print(root.val, end="")
        self.printTree(root.right)
        
    def invertTree(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(7, TreeNode(6), TreeNode(9))

obj = Solution()
obj.printTree(root)
obj.invertTree(root)
obj.printTree(root)