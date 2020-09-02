# https://leetcode.com/problems/generate-parentheses/
# https://leetcode.com/problems/generate-parentheses/discuss/820807/easy-python

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution:
    def generateParenthesis(self, n):
        def dfs(s, res, open_, close):
            if open_ == 0 and close == 0:
                res.append(s)
            if open_ > 0:
                dfs(s+"(", res, open_-1, close)
            if open_ < close:
                dfs(s+")", res, open_, close-1)
            return
        
        res = []
        dfs("", res, n, n)
        return res

n = 3
result = Solution().generateParenthesis(n)
print(result)