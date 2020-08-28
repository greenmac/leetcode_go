# https://leetcode.com/problems/queue-reconstruction-by-height/
# https://hackmd.io/@kenjin/rktSqAFDS
# https://blog.csdn.net/fuxuemingzhu/article/details/68486884
# https://www.itread01.com/content/1546797429.html

'''
406. Queue Reconstruction by Height
Medium

3303

372

Add to List

Share
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people or not people[0]:
            return []
        temp_people = sorted(people, key = lambda people:(-people[0], people[1]))
        print(temp_people)
        res = []
        for man in temp_people:
            # print(man[1])
            res.insert(man[1], man)
        return res

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
result = Solution().reconstructQueue(people)
print(result)