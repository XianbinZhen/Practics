# Given a singly - linked list, reverse the
# list. This can be done iteratively or recursively.Can you get both solutions?
#
# Example:
# Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
#
#
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#     # Function to print the list
#     def printList(self):
#         node = self
#         output = ''
#         while node != None:
#             output += str(node.val)
#             output += " "
#             node = node.next
#         print(output)
#
#     # Iterative Solution
#     def reverseIteratively(self, head):
#
#     # Implement this.
#
#     # Recursive Solution
#     def reverseRecursively(self, head):
#
#
# # Implement this.
#
# # Test Program
# # Initialize the test list:
# testHead = ListNode(4)
# node1 = ListNode(3)
# testHead.next = node1
# node2 = ListNode(2)
# node1.next = node2
# node3 = ListNode(1)
# node2.next = node3
# testTail = ListNode(0)
# node3.next = testTail
#
# print("Initial list: ")
# testHead.printList()
# # 4 3 2 1 0
# testHead.reverseIteratively(testHead)
# # testHead.reverseRecursively(testHead)
# print("List after reversal: ")
# testTail.printList()
# # 0 1 2 3 4

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    def reverseIteratively(self, head):
        arr = [head]
        node = head
        node = node.next
        while node:
            arr.append(node)
            node = node.next
        i = len(arr) - 1
        tail = arr[i]
        while i > 0:
            tail.next = arr[i - 1]
            tail = tail.next
            i -= 1
        tail.next = None

    # Recursive Solution
    def reverseRecursively(self, head):
        def reverse(current_node, next_node):
            # print("current node: ", current_node.val)
            # print("next node: ", next_node.val)
            if next_node:
                if next_node.next:
                    temp_node = next_node.next
                    next_node.next = current_node
                    reverse(next_node, temp_node)
                else:
                    next_node.next = current_node

        reverse(head, head.next)
        head.next = None


# Implement this.

# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
# testHead.reverseIteratively(testHead)
testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4
