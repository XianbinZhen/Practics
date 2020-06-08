# You are given an array of integers.
# Return an array of the same size where the element at each
# index is the product of all the elements in the original array except for the element at that index.
#
# For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].
#
# You cannot use division in this problem.
#
# Here's a start:
# def products(nums):
#   # Fill this in.
#
# print products([1, 2, 3, 4, 5])
# # [120, 60, 40, 30, 24]

def products(nums):
    result_arr = []
    for i in range(len(nums)):
        result = 1
        for j in range(len(nums)):
            if i == j:
                pass
            else:
                result *= nums[j]
        result_arr.append(result)
    return result_arr


print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
