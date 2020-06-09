# You are given the root of a binary tree.
# Return the deepest node (the furthest node from the root).
#
# Example:
#     a
#    / \
#   b   c
#  /
# d
#
# The deepest node in this tree is d at depth 3.
#
# Here's a starting point:
# class Node(object):
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
#
#   def __repr__(self):
#     # string representation
#     return self.val
#
#
# def deepest(node):
#   # Fill this in.
#
# root = Node('a')
# root.left = Node('b')
# root.left.left = Node('d')
# root.right = Node('c')
#
# print deepest(root)
# # (d, 3)

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(root):
    def tree_depth(root):
        if root:
            return max(tree_depth(root.left) + 1, tree_depth(root.right) + 1)
        else:
            return 0

    def find_node_in_depth(root, depth):
        # print("depth: ", depth)
        # print("node: ", root.val)
        if depth == 1:
            # print("return: ", root.val)
            return root
        else:
            if root.left:
                return find_node_in_depth(root.left, depth - 1)
            if root.right:
                return find_node_in_depth(root.right, depth - 1)

    depth = tree_depth(root)

    node = find_node_in_depth(root, depth)
    return (node, depth)


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
# root.left.right = Node('e')
root.right = Node('c')

print(deepest(root))
# (d, 3)
