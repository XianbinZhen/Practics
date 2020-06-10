# You have a landscape, in which puddles can form.
# You are given an array of non-negative integers representing the elevation at each location.
# Return the amount of water that would accumulate if it rains.
#
# For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
#        X
#    X███XX█X
#  X█XX█XXXXXX
# # [0,1,0,2,1,0,1,3,2,1,2,1]
# Here's your starting pont:
# def capacity(arr):
#   # Fill this in.
#
# print capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# # 6

def capacity(arr):
    arr2 = arr.copy()
    arr2.sort()
    set1 = set(arr2)
    trapped = 0
    for i in set1:
        if i > 0:
            # print("height: ", i)
            start_count = False
            start = 0
            end = 0
            for j in range(len(arr)):
                # print("arr height: ", arr[j])
                if arr[j] >= i:
                    if not start_count:
                        start = j
                        start_count = True
                    else:
                        end = j
                        start_count = False
                if end > start:
                    trapped = trapped + end - start - 1
                    # print("traped: ", trapped)
                    start = end
                    start_count = True
    return trapped


print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
