# You are given a stream of numbers. Compute the median for each new element .
# Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]
# Here's a starting point:
# def running_median(stream):
#   # Fill this in.
# running_median([2, 1, 4, 7, 2, 0, 5])
# # 2 1.5 2 3.0 2 2.0 2

def running_median(stream):
    result = []
    result.append(stream[0])
    for i in range(1, len(stream)):
        # print("index: ", i)
        temp_stream = stream[:i + 1]
        temp_stream.sort()
        # print("temp stream: ", temp_stream)
        length = len(temp_stream)
        median_index = int(length / 2)
        # print("length ", length)
        # print("median index: ", median_index)
        if length % 2 == 0:
            result.append((temp_stream[median_index] + temp_stream[median_index - 1]) / 2)
        else:
            result.append(temp_stream[median_index])
    return result


print(running_median([2, 1, 4, 7, 2, 0, 5]))
# 2 1.5 2 3.0 2 2.0 2
