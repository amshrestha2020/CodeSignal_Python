def solution(sequence):
    def is_increasing(arr):
        return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))

    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            # Check if removing current or next element results in increasing sequence
            if is_increasing(sequence[:i] + sequence[i + 1:]) or is_increasing(sequence[:i + 1] + sequence[i + 2:]):
                return True
            else:
                return False

    return True

