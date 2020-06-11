# ou are given an array of integers.
# Return the length of the longest increasing subsequence (not necessarily contiguous) in the array.
#
# Example:
# [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
#
# The following input should return 6 since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.

def longest_increasing_subsequece(arr):
    def opt(opt_arr, input_arr, index):
        if index == 0:
            return 1
        else:
            index_arr = []
            for i in range(index + 1):
                if input_arr[index] > input_arr[i]:
                    index_arr.append(i)
            if input_arr > 0:
                opt_value = 0
                for j in index_arr:
                    if opt_arr[j] > opt_value:
                        opt_value = opt_arr[j]
                return opt_value + 1
            else:
                return 0

    longest_length = []
    for k in range(len(arr)):
        longest_length.append(1)
    for l_index in range(1, len(arr)):
        longest_length[l_index] = opt(longest_length, arr, l_index)
    print(longest_length)
    return max(longest_length)


arr1 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(longest_increasing_subsequece(arr1))
