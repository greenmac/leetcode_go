# https://leetcode.com/problems/invert-binary-tree/
# https://leetcode.com/problems/invert-binary-tree/discuss/812839/Python-Recursive-Simple-Solution

'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        root = TreeNode(root)
        if root == None:
            return None
        Left = self.invertTree(root.left)
        Right = self.invertTree(root.right)
        root.left = Right
        root.right = Left
        return root

# root = [4,2,7,1,3,6,9]
# result = Solution().invertTree(root)
# print(result)