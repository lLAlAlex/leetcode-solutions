# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.preIndex = 0
        self.postIndex = 0
        
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.constructTree(preorder, postorder)
    
    def constructTree(self, preorder, postorder):
        root = TreeNode(preorder[self.preIndex])
        self.preIndex += 1
        
        if root.val != postorder[self.postIndex]:
            root.left = self.constructTree(preorder, postorder)
        
        if root.val != postorder[self.postIndex]:
            root.right = self.constructTree(preorder, postorder)
        
        self.postIndex += 1
        
        return root

obj = Solution()
obj.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1])