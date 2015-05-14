def is_increasing(seq):
    return all([seq[i] > seq[i-1] for i in range(1, len(seq))])

