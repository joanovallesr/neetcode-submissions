# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        inorder_map = {node_val: idx for idx, node_val in enumerate(inorder)}

        def helper(j, k):
            if not 0 <= j <= k:
                return None

            node_val = preorder[self.i]
            self.i += 1

            node = TreeNode(node_val)
            idx = inorder_map[node_val]
            node.left = helper(j, idx-1)
            node.right = helper(idx+1, k)

            return node
        
        return helper(0, len(inorder)-1)
            