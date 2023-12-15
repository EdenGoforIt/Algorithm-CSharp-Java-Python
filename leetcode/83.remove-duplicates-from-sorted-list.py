#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
from typing import List


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def createList(vals: List[int]) -> ListNode:
#     head = ListNode(vals[0])
#     temp_node = head
#     for i in range(1, len(vals)):
#         temp_node.next = ListNode(vals[i])
#         temp_node = temp_node.next
#     return head


# def showList(l: ListNode):
#     list_string = ''
#     while l:
#         list_string += str(l.val)
#         l = l.next
#         if l:
#             list_string += " -> "
#     print(list_string)
#     return list_string


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        # print(head)
        return head


# ll = createList([1, 1, 2])
# ll2 = createList([1, 1, 2, 3, 3])
# print(Solution().deleteDuplicates(ll2))
# print(Solution().deleteDuplicates(ll))

# @lc code=end
