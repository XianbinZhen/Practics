# Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c)
# in nums such that a + b + c = 0. Note that there may not be any triplets
# that sum to zero in nums, and that the triplets must not be duplicates.
# Example:
# Input: nums = [0, -1, 2, -3, 1]
# Output: [0, -1, 1], [2, -3, 1]
# Here's a starting point:
# class Solution(object):
#   def threeSum(self, nums):
#     # Fill this in.
# # Test Program
# nums = [1, -2, 1, 0, 5]
# print(Solution().threeSum(nums))
# # [[-2, 1, 1]]

class Solution(object):
    def threeSum(self, nums):
        length = len(nums)
        result = []
        if length >= 3:
            for i in range(length - 2):
                for j in range(i + 1, length - 1):
                    for k in range(j + 1, length):
                        if nums[i] + nums[j] + nums[k] == 0:
                            result.append([nums[i], nums[j], nums[k]])
        return result


# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]
