# https://leetcode.com/problems/daily-temperatures/
# https://leetcode.com/problems/daily-temperatures/discuss/813154/Python%3A-forward-stack-solution-(412-428-ms-94-98)
# https://medium.com/tomsnote/leetcode-739-daily-temperatures-70e003af6116

'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
'''
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        wait = [0]*len(T)
        stack = []
        
        for i, x in enumerate(T):
            while stack and x > T[stack[-1]]:
                j = stack.pop()
                wait[j] = i - j
            stack.append(i)
        return wait

T = [73, 74, 75, 71, 69, 72, 76, 73]
result = Solution().dailyTemperatures(T)
print(result)