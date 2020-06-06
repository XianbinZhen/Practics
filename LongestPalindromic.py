# A palindrome is a sequence of characters that reads the same backwards and forwards.
# Given a string, s, find the longest palindromic substring in s.
# Example:
# Input: "banana"
# Output: "anana"
# Input: "million"
# Output: "illi"
# class Solution:
#     def longestPalindrome(self, s):
# # Fill this in.
# # Test program
# s = "tracecars"
# print(str(Solution().longestPalindrome(s)))
# # racecar

class Solution:
    def longestPalindrome(self, s):
        result = ''
        for i in range(len(s)):
            # print("finding from: ", s[i])
            c = s[i]
            last_index = s.rindex(c)
            temp = s[i:last_index + 1]
            while temp:
                palindrome = temp
                # print("palindrome: ", palindrome)
                if palindrome == palindrome[::-1]:
                    if len(palindrome) > len(result):
                        result = palindrome
                temp = palindrome[:len(palindrome) - 1]
                if c in temp:
                    last_index = temp.rindex(c)
                    temp = temp[:last_index + 1]
                    # print("temp: ", temp)
                else:
                    temp = ''
        return result


s = "tracecars"
# s = "b1231anana111"
print(str(Solution().longestPalindrome(s)))
# racecar
