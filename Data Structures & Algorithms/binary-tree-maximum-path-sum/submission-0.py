# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
                
            left_max_path = max(dfs(root.left), 0)
            right_max_path = max(dfs(root.right), 0)
            root_is_max = root.val + left_max_path + right_max_path
            self.max_sum = max(root_is_max, self.max_sum)

            return root.val + max(left_max_path, right_max_path)
        
        self.max_sum = float('-inf')
        dfs(root)
        return self.max_sum