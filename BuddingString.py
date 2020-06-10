# Given two strings A and B of lowercase letters,
# return true if and only if we can swap two letters in A so that the result equals B.
#
# Example 1:
# Input: A = "ab", B = "ba"
# Output: true
# Example 2:
#
# Input: A = "ab", B = "ab"
# Output: false
# Example 3:
# Input: A = "aa", B = "aa"
# Output: true
# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:
# Input: A = "", B = "aa"
# Output: false
# Here's a starting point:
# class Solution:
#   def buddyStrings(self, A, B):
#     # Fill this in.
#
# print Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb')
# # True
# print Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb')
# # False

class Solution:
    def buddyStrings(self, A, B):
        difference = []
        for i in range(len(A)):
            if A[i] == B[i]:
                pass
            else:
                difference.append(A[i])
                difference.append(B[i])
        if len(difference) == 4:
            if difference[0] == difference[3] and difference[1] == difference[2]:
                return True
        else:
            return False


print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
