# Given a string,
# you need to reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "The cat in the hat"
# Output: "ehT tac ni eht tah"
# Note: In the string, each word is separated by single space
# and there will not be any extra space in the string.
#
# Here's a starting point:
# class Solution:
#   def reverseWords(self, str):
#     # Fill this in.
#
# print Solution().reverseWords("The cat in the hat")
# # ehT tac ni eht tah

class Solution:
    def reverseWords(self, str):
        result_str = str.split(" ")
        for i in range(len(result_str)):
            result_str[i] = result_str[i][::-1]
        result = result_str[0]
        result_str = result_str[1:]
        while result_str:
            result += " "
            result += result_str[0]
            result_str = result_str[1:]
        return result


print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
