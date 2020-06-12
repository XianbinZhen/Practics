# Given a sorted list of numbers, change it into a balanced binary search tree.
# You can assume there will be no duplicate numbers in the list.
#
# Here's a starting point:
# from collections import deque
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
#   def __str__(self):
#     # level-by-level pretty-printer
#     nodes = deque([self])
#     answer = ''
#     while len(nodes):
#       node = nodes.popleft()
#       if not node:
#         continue
#       answer += str(node.value)
#       nodes.append(node.left)
#       nodes.append(node.right)
#     return answer
#
#
# def createBalancedBST(nums):
#   # Fill this in.
#
# print createBalancedBST([1, 2, 3, 4, 5, 6, 7])
# # 4261357
# #   4
# #  / \
# # 2   6
# #/ \ / \
# #1 3 5 7

from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer


# def insert(root, key):
#     if key < root.value:
#         if root.left is None:
#             root.left = Node(key)
#         else:
#             insert(root.left, key)
#     elif key > root.value:
#         if root.right is None:
#             root.right = Node(key)
#         else:
#             insert(root.right, key)
#     else:
#         print("error!")


def insert(node, value):
    if value < node.value:
        if node.left:
            insert(node.left, value)
        else:
            node.left = Node(value)
    else:
        if node.right:
            insert(node.right, value)
        else:
            node.right = Node(value)


def createBalancedBST(nums):
    def middle_sort(arr, nums):
        if nums:
            if len(nums) == 1:
                arr.append(nums[0])
            else:
                mid_point = int(len(nums) / 2)
                arr.append(nums[mid_point])
                middle_sort(arr, nums[:mid_point])
                middle_sort(arr, nums[mid_point + 1:])
    temp_arr = []
    middle_sort(temp_arr, nums)
    # print("middle sort: ", temp_arr)
    root = Node(temp_arr[0])
    for i in range(1, len(temp_arr)):
        insert(root, temp_arr[i])
    return root


print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))
# 4261357
#   4
#  / \
# 2   6
# / \ / \
# 1 3 5 7
