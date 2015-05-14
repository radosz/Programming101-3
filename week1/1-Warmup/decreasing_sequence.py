def is_decreasing(seq):
    return all([seq[i] < seq[i-1] for i in range(1, len(seq))])
