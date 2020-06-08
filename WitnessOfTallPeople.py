# There are n people lined up, and each have a height represented as an integer.
# A murder has happened right in front of them, and only people who are
# taller than everyone in front of them are able to see what has happened. How many witnesses are there?
#
# Example:
# Input: [3, 6, 3, 4, 1]
# Output: 3
# Explanation: Only [6, 4, 1] were able to see in front of them.
#  #
#  #
#  # #
# ####
# ####
# #####
# 36341                                 x (murder scene)
# Here's your starting point:
# def witnesses(heights):
#   # Fill this in.
#
# print witnesses([3, 6, 3, 4, 1])
# # 3

def witnesses(heights):
    i = len(heights) - 1
    wall = heights.copy()
    wall[i] = 0
    i -= 1
    while i >= 0:
        # print("i: ", i)
        wall[i] = max(heights[i + 1], wall[i + 1])
        # print(heights[i + 1])
        i -= 1
    result = []
    for j in range(len(heights)):
        if wall[j] < heights[j]:
            result.append(heights[j])
    # print(wall)
    return len(result)


print(witnesses([3, 6, 3, 4, 1]))
# 3
