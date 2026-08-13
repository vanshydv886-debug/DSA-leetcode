# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
     def maxPathSum(self, root):
        self.maxi = float('-inf')

        def solve(node):
            if node is None:
                return 0

            leftSum = solve(node.left)
            if leftSum < 0:
                leftSum = 0

            rightSum = solve(node.right)
            if rightSum < 0:
                rightSum = 0

            self.maxi = max(self.maxi, leftSum + node.val + rightSum)

            return node.val + max(leftSum, rightSum)

        solve(root)
        return self.maxi