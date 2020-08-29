# https://leetcode.com/problems/permutations/
# https://leetcode.com/problems/permutations/discuss/814320/Python-Easy-to-understand-recursive-solution-with-comments-faster-than-81

'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
def helper(arr):
    # print('arr:', arr, 'len_arr:', len(arr))
    #Take care of base cases
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    #Stores all results
    res = []
    #Iterate over each element
    for i in range(len(arr)):
        #Form a new array excluding the current element
        leftOver = arr[:i] + arr[i+1:]
        # print('i:', i, 'leftOver:', leftOver, 'arr[:i]:', arr[:i], 'arr[i+1:]:', arr[i+1:])
        #Permute the new array and add the currently
        #excluded element into the list of all permutations 
        for p in helper(leftOver):
            res.append([arr[i]] + p)
            # print('p:', p, 'res:', res)
            # print("="*40)
    return res 

class Solution:
    def permute(self, nums):
        return helper(nums)

nums = [1,2,3]
result = Solution().permute(nums)
print(result)