# Given an array with n objects colored red, white or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the
# color red, white, and blue respectively.
# Note: You are not suppose to use the library’s sort function for this problem.
# Can you do this in a single pass?
# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Here's a starting point:
# class Solution:
#   def sortColors(self, nums):
#     # Fill this in.
# nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
# print("Before Sort: ")
# print(nums)
# # [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
# Solution().sortColors(nums)
# print("After Sort: ")
# print(nums)
# # [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]

class Solution:
    def quick_sort(self, arr, low, high):
        if (low < high):
            pi = Solution.partition(self, nums, low, high)
            Solution.quick_sort(self, arr, low, pi - 1)
            Solution.quick_sort(self, arr, pi + 1, high)

    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i = 1 + i
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def sortColors(self, nums):
        Solution.quick_sort(self, nums, 0, len(nums) - 1)


def q_sort(arr, low, high):
    if low < high:
        pivot = q_partition(arr, low, high)
        q_sort(arr, low, pivot - 1)
        q_sort(arr, pivot + 1, high)


def q_partition(arr, low, high):
    low_index = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            low_index += 1
            arr[low_index], arr[j] = arr[j], arr[low_index]
    low_index += 1
    arr[low_index], arr[high] = arr[high], arr[low_index]
    return low_index


nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
# q_sort(nums, 0, len(nums) - 1)
print("After Sort: ")
print(nums)

# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
