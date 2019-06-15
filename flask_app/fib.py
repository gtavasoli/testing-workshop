""" Fibonacci calculator """


def get(number):
    """ Generate fib sequence until specified number is exceeded """
    # Seed the sequence with 0 and 1
    sequence = [0, 1]
    while sequence[-1] < number:
        sequence.append(sequence[-2] + sequence[-1])
    return sequence
