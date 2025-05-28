# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class FindElements(object):

    def __init__(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        """
        self.seen = set()
        self.dfs(root, 0)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.seen
        
    def dfs(self, node: TreeNode, value):
        if node is None:
            return
        
        self.seen.add(value)
        self.dfs(node.left, value * 2 + 1)
        self.dfs(node.right, value * 2 + 2)