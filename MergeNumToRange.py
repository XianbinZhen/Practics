# Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.
#
# Example:
# Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
# Output: ['0->2', '5->5', '7->11', '15->15']
# Assume that all numbers will be greater than or equal to 0, and each element can repeat.
#
# Here is a starting point:
# def findRanges(nums):
#   # Fill this in.
#
# print findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15])
# # ['0->2', '5->5', '7->11', '15->15']

def findRanges(nums):
    def arr2List(arr):
        return str(arr[0]) + "->" + str(arr[-1])

    result = []
    temp_list = [nums[0]]
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            pass
        elif nums[i] + 1 == nums[i + 1]:
            temp_list.append(nums[i + 1])
        else:
            result.append(temp_list)
            temp_list = [nums[i + 1]]
    result.append(temp_list)
    for i in range(len(result)):
        result[i] = arr2List(result[i])
    return result


print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']
