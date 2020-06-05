# You are given an array of tuples (start, end) representing time intervals for lectures.
# The intervals may be overlapping. Return the number of rooms that are required.
#
# For example. [(30, 75), (0, 50), (60, 150)] should return 2.

def room_schedule(lectures):
    room = [[]]
    room[0].append(lectures[0])
    for i in range(1, len(lectures)):
        # print("lecture i: ", lectures[i])
        length = len(room)
        j = 0
        while j < length:
            if not is_overlap(lectures[i], room[j]):
                room[j].append(lectures[i])
                j = length + 1
            else:
                j += 1
            if j == length:
                room.append([lectures[i]])
    # print(room)
    return len(room)


def is_overlap(tup, arr):
    for a in arr:
        if a[0] < tup[0] < a[1] or a[0] < tup[1] < a[1] or tup[0] <= a[0] and tup[1] >= a[1]:
            return True
    return False


test = [(30, 75), (0, 50), (60, 150), (150, 160), (140, 141), (60, 70), (30, 50), (31, 32)]
print(room_schedule(test))
