# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        rst = 0
        if root.left:
            rst += self.rangeSumBST(root.left, L, R)

        if root.right:
            rst += self.rangeSumBST(root.right, L, R)

        return rst + root.val if L <= root.val and root.val <= R else rst
