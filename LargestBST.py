# You are given the root of a binary tree.
# Find and return the largest subtree of that tree,
# which is a valid binary search tree.
# Here's a starting point:
# class TreeNode:
#   def __init__(self, key):
#     self.left = None
#     self.right = None
#     self.key = key
#   def __str__(self):
#     # preorder traversal
#     answer = str(self.key)
#     if self.left:
#       answer += str(self.left)
#     if self.right:
#       answer += str(self.right)
#     return answer
# def largest_bst_subtree(root):
#   # Fill this in.
# #     5
# #    / \
# #   6   7
# #  /   / \
# # 2   4   9
# node = TreeNode(5)
# node.left = TreeNode(6)
# node.right = TreeNode(7)
# node.left.left = TreeNode(2)
# node.right.left = TreeNode(4)
# node.right.right = TreeNode(9)
# print largest_bst_subtree(node)
# #749
import sys


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer


def largest_bst_subtree(root):
    def inorder_traverse(root, result):
        if root is not None:
            inorder_traverse(root.left, result)
            result.append(root.key)
            inorder_traverse(root.right, result)

    def longest_sub_sequence(result):
        result_sequence = []
        sequence = []
        pre_val = -sys.maxsize - 1
        length = 0
        for i in range(len(result)):
            if result[i] > pre_val:
                length += 1
                sequence.append(result[i])
                pre_val = result[i]
                longest_length = length
                if length >= longest_length:
                    result_sequence = sequence
            else:
                # print("current_val:", result[i])
                length = 1
                sequence = [result[i]]
                pre_val = result[i]
        return result_sequence

    def insert(root, key):
        if key < root.key:
            if root.left is None:
                root.left = TreeNode(key)
            else:
                insert(root.left, key)
        elif key > root.key:
            if root.right is None:
                root.right = TreeNode(key)
            else:
                insert(root.right, key)
        else:
            print("error!")

    # def insert(root, node):
    #     if root is None:
    #         root = node
    #     else:
    #         if root.key < node.key:
    #             if root.right is None:
    #                 root.right = node
    #             else:
    #                 insert(root.right, node)
    #         else:
    #             if root.left is None:
    #                 root.left = node
    #             else:
    #                 insert(root.left, node)

    result = []
    inorder_traverse(root, result)
    result_sequence = longest_sub_sequence(result)
    # tree = TreeNode(result_sequence[0])
    tree = TreeNode(result_sequence[0])
    for i in range(1, len(result_sequence)):
        insert(tree, result_sequence[i])
    return tree


node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
node.right.right.right = TreeNode(19)
node.right.right.left = TreeNode(8)
print(largest_bst_subtree(node))
# 749
