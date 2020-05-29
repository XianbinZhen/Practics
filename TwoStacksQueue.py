# Implement a queue class using two stacks.
# A queue is a data structure that supports the FIFO protocol
# (First in = first out).Your class should support the enqueue and dequeue methods like a standard queue.
# Here's a starting point:
# class Queue:
#     def __init__(self):
#     # Fill this in.
#     def enqueue(self, val):
#     # Fill this in.
#     def dequeue(self):
# # Fill this in.
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print q.dequeue()
# print q.dequeue()
# print q.dequeue()
# # 1 2 3

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        val = self.queue[0]
        self.queue = self.queue[1:]
        return val


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3
