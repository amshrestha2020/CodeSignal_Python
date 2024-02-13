def solution(blockCount, writes, threshold):
    # Initialize the number of writes for each block
    writes_count = [0] * blockCount

    # Update the number of writes for each block
    for start, end in writes:
        writes_count[start] += 1
        if end + 1 < blockCount:
            writes_count[end + 1] -= 1

    # Calculate the prefix sum of writes_count
    for i in range(1, blockCount):
        writes_count[i] += writes_count[i - 1]

    # Find the disjoint segments of blocks that have reached the rewrite threshold
    segments = []
    segment_start = -1
    for i in range(blockCount):
        if writes_count[i] >= threshold and segment_start == -1:
            segment_start = i
        elif writes_count[i] < threshold and segment_start != -1:
            segments.append([segment_start, i - 1])
            segment_start = -1
    if segment_start != -1:
        segments.append([segment_start, blockCount - 1])

    return segments
