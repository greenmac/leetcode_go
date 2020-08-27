# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/34212/1-line-Ruby-and-Python

'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''
# 二元樹的盡量不碰
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0

# A = [3,9,20,None,None,15,7]
# B = Solution().maxDepth(A)
# print(B)