# Contiguous Subarray with Maximum Sum
# You are given an array of integers.
# Find the maximum sum of all possible contiguous subarrays of the array.
#
# Example:
#
# [34, -50, 42, 14, -5, 86]
#
# Given this input array, the output should be 137.
# The contiguous subarray with the largest sum is[42, 14, -5, 86].
#
# Your solution should run in linear time.
#
# Here 's a starting point:
# def max_subarray_sum(arr):
# # Fill this in.
# print
# max_subarray_sum([34, -50, 42, 14, -5, 86])
# # 137

def max_subarray_sum(arr):
    opt_arr = arr.copy()
    for i in range(1, len(opt_arr)):
        opt_arr[i] = max(arr[i], opt_arr[i - 1] + arr[i])
    print(opt_arr)
    return max(opt_arr)


print(max_subarray_sum([34, -50, -1, 42, 14, -5, 86]))
# 137
