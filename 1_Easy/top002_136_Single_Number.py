# https://leetcode.com/problems/single-number/
# https://leetcode.com/problems/single-number/discuss/43000/Python-different-solutions.
'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''
# XOR( ^= 相關解釋)
# http://www.86duino.com/?p=1411&lang=TW
# https://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_XOR.html
# https://medium.com/@hyWang/xor-%E4%BD%8D%E5%85%83%E9%81%8B%E7%AE%97%E5%AD%90-1c25b4ae15fb
class Solution:
    def singleNumber(self, nums):
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]            
        return nums[0]
        
Solution = Solution()
nums_1 = [2,2,1]
nums_2 = [4,1,2,1,2]
singleNumber_1 = Solution.singleNumber(nums_1)
singleNumber_2 = Solution.singleNumber(nums_2)
print(singleNumber_1)
print(singleNumber_2)