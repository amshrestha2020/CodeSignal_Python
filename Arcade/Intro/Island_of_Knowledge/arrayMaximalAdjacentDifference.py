def solution(inputArray):
    max_difference = 0
    
    for i in range(len(inputArray) - 1):
        difference = abs(inputArray[i] - inputArray[i + 1])
        max_difference = max(max_difference, difference)
    
    return max_difference

