# You are given an array of k sorted singly linked lists.
# Merge the linked lists into a single sorted linked list and return it.
# Here's your starting point:
# class Node(object):
#   def __init__(self, val, next=None):
#     self.val = val
#     self.next = next
#   def __str__(self):
#     c = self
#     answer = ""
#     while c:
#       answer += str(c.val) if c.val else ""
#       c = c.next
#     return answer
# def merge(lists):
#   # Fill this in.
# a = Node(1, Node(3, Node(5)))
# b = Node(2, Node(4, Node(6)))
# print merge([a, b])
# # 123456

import sys


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) + " " if c.val else " "
            c = c.next
        return answer


def merge(lists):
    smallest_value_index = 0
    result_node = Node(-1)
    current_node = result_node
    more = True
    changed = False
    while more:
        smallest_value = sys.maxsize
        for i in range(len(lists)):
            if lists[i] is not None:
                print("node is: ", lists[i])
                current_value = lists[i].val
                if current_value <= smallest_value:
                    smallest_value = current_value
                    smallest_value_index = i
                    changed = True
        if changed:
            print("changed!")
            lists[smallest_value_index] = lists[smallest_value_index].next
            current_node.next = Node(smallest_value)
            current_node = current_node.next
            changed = False
            print("result list: ", result_node)
        more = False
        for node in lists:
            print("updated node: ", node)
            if node is not None:
                more = True
                break

    return result_node.next


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
# print(a.next)
# 123456
