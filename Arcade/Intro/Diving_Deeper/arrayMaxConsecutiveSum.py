def solution(inputArray, k):
    n = len(inputArray)

    # Initialize the initial sum for the first subarray of length k
    current_sum = sum(inputArray[:k])
    max_sum = current_sum

    # Slide the window through the array
    for i in range(k, n):
        # Update the current sum by removing the leftmost element and adding the rightmost element
        current_sum = current_sum - inputArray[i - k] + inputArray[i]
        max_sum = max(max_sum, current_sum)

    return max_sum

