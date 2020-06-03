# You are given a string s, and an integer k.
# Return the length of the longest substring in s that contains at most k distinct characters.
#
# For instance, given the string:
# aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff.
# The answer should be 5.
#
# Here's a starting point:
# def longest_substring_with_k_distinct_characters(s, k):
#   # Fill this in.
#
# print longest_substring_with_k_distinct_characters('aabcdefff', 3)
# # 5 (because 'defff' has length 5 with 3 characters)

def longest_substring_with_k_distinct_characters(s, k):
    longest_length = 1
    longest_substring = []
    for i in range(k):
        longest_substring.append([])
    temp_k = 0
    prev_str = s[0]
    index = 0
    while index < len(s):
        # print("string is:", s[index])
        if s[index] == prev_str:
            longest_substring[temp_k].append(prev_str)
        else:
            temp_k += 1
            temp_k %= k
            longest_substring[temp_k] = []
            longest_substring[temp_k].append(s[index])
            prev_str = s[index]
        index += 1
        length = 0
        # print("longest substring: ", longest_substring)
        for arr in longest_substring:
            length += len(arr)
        if length > longest_length:
            longest_length = length
            result_string = longest_substring
        # print("longest length is:", longest_length)
    return longest_length


print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
