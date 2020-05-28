# You are given the preorder and inorder traversals of a binary tree in the form of arrays.
# Write a function that reconstructs the tree represented by these traversals.
# Example:
# Preorder: [a, b, d, e, c, f, g]
# Inorder: [d, b, e, a, f, c, g]
# The tree that should be constructed from these traversals is:
#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g
# Here's a start:
# from collections import deque
# class Node(object):
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
#   def __str__(self):
#     q = deque()
#     q.append(self)
#     result = ''
#     while len(q):
#       n = q.popleft()
#       result += n.val
#       if n.left:
#         q.append(n.left)
#       if n.right:
#         q.append(n.right)
#     return result
# def reconstruct(preorder, inorder):
#   # Fill this in.
# tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
#                    ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
# print tree
# # abcdefg


from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return result


def reconstruct(preorder, inorder):
    def insert(root, leaf, inorder):
        # print("insert: ", leaf)
        current_node = root
        new_node = Node(leaf)
        current_value = inorder.index(current_node.val)
        new_value = inorder.index(leaf)
        if new_value <= current_value:
            if current_node.left is None:
                # print("insert ", leaf, " to the left")
                current_node.left = new_node
            else:
                # print("move left")
                insert(current_node.left, leaf, inorder)
        else:
            if current_node.right is None:
                # print("insert ", leaf, " to the right")
                current_node.right = new_node
            else:
                # print("move right")
                insert(current_node.right, leaf, inorder)

    root = Node(preorder[0])
    for i in range(1, len(preorder)):
        leaf = preorder[i]
        insert(root, leaf, inorder)
    return root


tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print(tree)
# abcdefg
