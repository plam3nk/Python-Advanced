# 05. Fibonacci Sequence

def create_sequence(count: int):
    nterms = count
    sequence = []
    # first two terms
    n1, n2 = 0, 1
    count = 0

    if nterms == 1:
        sequence.append(n1)

    else:
        while count < nterms:
            sequence.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
    return sequence


def locate(number, *sequence):
    for i in range(len(sequence)):
        if int(number) == sequence[i]:
            return i

    else:
        return False
    