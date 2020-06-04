# Given a string, find the length of the longest substring without repeating characters.
#
# Here is an example solution in Python language.
# (Any language is OK to use in an interview,
# though we'd recommend Python as a generalist language utilized by companies like Google, '
# 'Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)
# class Solution:
#   def lengthOfLongestSubstring(self, s):
#     # Fill this in.
#
# print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# # 10

class Solution:
    def lengthOfLongestSubstring(self, s):
        result = 0
        start_index = 0
        result_substring = []
        longest_substring = []
        for index in range(len(s) - 1):
            if s[index] == s[index + 1]:
                result_substring = s[start_index:index + 1]
                start_index = index + 1
                if len(result_substring) > result:
                    result = len(result_substring)
                    longest_substring = result_substring
        return result


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
