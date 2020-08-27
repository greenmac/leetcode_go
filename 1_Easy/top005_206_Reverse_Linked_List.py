# https://leetcode.com/problems/reverse-linked-list/
# https://leetcode.com/problems/reverse-linked-list/discuss/811221/Python-Iterative-and-Recursive-Solutions

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head = ListNode(next=head)
        cur_node = head
        prev = None
        
        while cur_node:
            next_cur = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next_cur
        return prev

head = [1,2,3,4,5]
# head = ListNode(next=head)
result = Solution().reverseList(head)
# print(result)