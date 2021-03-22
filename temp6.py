def pingpong(x):
    index = 1  # index
    sequence = 1  # counting the sequence

    while index <= x:
        sequence += 1

        if x <= 8:
            sequence = sequence - 1

        elif count % 8 == 0 or '8' in str(sequence - 1):
            sequence -= 1
        else:
            sequence += 1
    return sequence


print(pingpong(30))