"""
A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term is obtained by describing the previous term. An example is easier to understand:
Each consecutive value describes the prior value.

1      #
11     # one 1's
21     # two 1's
1211   # one 2, and one 1.
111221 # #one 1, one 2, and two 1's.

Your task is, return the nth term of this sequence.
"""


def look_and_say_seq(nth):
    sequence = [1]
    for n in range(1, nth + 1):
        sequence = calculate_sequence([], sequence)
    return sequence


def calculate_sequence(preq, sequence):
    if sequence:
        print("sequence is: ", sequence)
        length = len(sequence)
        start = sequence[0]
        count = 1
        for n in range(1, length):
            if start != sequence[n]:
                count = n
                print("start is: ", start, "count is: ", count)
                break
            else:
                count += 1
        preq.append(count)
        preq.append(start)

        print("preq is: ", preq)
        return calculate_sequence(preq, sequence[count:])
    else:
        return preq

#
# seq1 = []
# seq2 = [1, 2, 1, 1]
# print(calculate_sequence(seq1, seq2))
print(look_and_say_seq(5))
