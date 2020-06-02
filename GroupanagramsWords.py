# Given a list of words, group the words that are anagrams of each other.
# (An anagram are words made up of the same letters).
# Example:
# Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
# Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]
# Here's a starting point:
# import collections
# def groupAnagramWords(strs):
#   # Fill this in.
# print groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg'])
# # [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]

import collections


def groupAnagramWords(strs):
    result = []
    while strs:
        str_set = [strs[0], ]
        strs.remove(strs[0])
        # print("str_set[0]: ", str_set)
        i = 0
        while i < len(strs):
            # print("index: ", i)
            # print("str: ", strs[i])
            if set(str_set[0]) == set(strs[i]):
                str_set.append(strs[i])
                strs.remove(strs[i])
                i -= 1
            i += 1
        result.append(str_set)
        # print("result: ", result)
    return result


print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
