# A unival tree is a tree where all the nodes have the same value. Given a binary tree,
# return the number of unival subtrees in the tree.
# For example, the following tree should return 5:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
# The 5 trees are:
# - The three single '1' leaf nodes. (+3)
# - The single '0' leaf node. (+1)
# - The [1, 1, 1] tree at the bottom. (+1)
# Here's a starting point:
# class Node(object):
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
# def count_unival_subtrees(root):
#   # Fill this in.
# a = Node(0)
# a.left = Node(1)
# a.right = Node(0)
# a.right.left = Node(1)
# a.right.right = Node(0)
# a.right.left.left = Node(1)
# a.right.left.right = Node(1)
# print count_unival_subtrees(a)
# # 5


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_unival_subtrees(root):
    if root is not None:
        count = 0
        if is_unival_tree(root):
            return number_of_nodes(root)
        else:
            return count_unival_subtrees(root.left) + count_unival_subtrees(root.right)
    else:
        return 0


def is_unival_tree(root):
    if root is None:
        return True
    else:
        value = root.val
        left_node = root.left
        right_node = root.right
        if left_node is not None:
            left_value = left_node.val
        else:
            left_value = value
        if right_node is not None:
            right_value = right_node.val
        else:
            right_value = value
        if value == left_value == right_value:
            return is_unival_tree(left_node) and is_unival_tree(right_node)
        else:
            return False


def number_of_nodes(root):
    if root is None:
        return 0
    else:
        return 1 + number_of_nodes(root.left) + number_of_nodes(root.right)


a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(1)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))
# 5
