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

def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res
    
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)
    
def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)
    
def singleNumber(self, nums):
    return reduce(operator.xor, nums)