# You are given two linked-lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Here is the function signature as a starting point (in Python):
# # Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#     self.val = x
#     self.next = None
#
# class Solution:
#   def addTwoNumbers(self, l1, l2, c = 0):
#     # Fill this in.
#
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
#
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
#
# result = Solution().addTwoNumbers(l1, l2)
# while result:
#   print result.val,
#   result = result.next
# # 7 0 8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        result_list = ListNode(-1)
        temp_list = result_list
        carry = c
        while l1 or l2:
            if l1 is None:
                l1_value = 0
            else:
                l1_value = l1.val
                l1 = l1.next
            if l2 is None:
                l2_value = 0
            else:
                l2_value = l2.val
                l2 = l2.next
            sum = l1_value + l2_value + carry
            carry = int(sum / 10)
            temp_list.next = ListNode(sum % 10)
            temp_list = temp_list.next
        if carry > 0:
            temp_list.next = ListNode(1)
        return result_list.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(4)
result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
# 7 0 8
