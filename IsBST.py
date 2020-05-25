# You are given the root of a binary search tree. Return true if
# it is a valid binary search tree, and false otherwise. Recall that
# a binary search tree has the property that all values in the left
# subtree are less than or equal to the root, and all values in the
# right subtree are greater than or equal to the root.
# Here's a starting point:
# class TreeNode:
#   def __init__(self, key):
#     self.left = None
#     self.right = None
#     self.key = key
#
# def is_bst(root):
#   # Fill this in.
#
# a = TreeNode(5)
# a.left = TreeNode(3)
# a.right = TreeNode(7)
# a.left.left = TreeNode(1)
# a.left.right = TreeNode(4)
# a.right.left = TreeNode(6)
# print is_bst(a)
#
# #    5
# #   / \
# #  3   7
# # / \ /
# #1  4 6

import sys


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def is_bst(root):
    result = True
    print("root is:", root.key)
    if root is None:
        return result
    else:
        if root.left is not None:
            left_key = root.left.key
            print("left key: ", left_key)
            # is_bst(root.left)
        else:
            left_key = -sys.maxsize - 1
            print("left key: ", left_key)
        if root.right is not None:
            right_key = root.right.key
            print("right key: ", right_key)
            # is_bst(root.right)
        else:
            right_key = sys.maxsize
            print("right key: ", right_key)
        if left_key >= root.key or root.key >= right_key:
            print("result is false!")
            return False
        else:
            if root.left is not None:
                result = result and is_bst(root.left)
            if root.right is not None:
                result = result and is_bst(root.right)
    return result


a = TreeNode(5)
a.left = TreeNode(13)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(8)
print(is_bst(a))
