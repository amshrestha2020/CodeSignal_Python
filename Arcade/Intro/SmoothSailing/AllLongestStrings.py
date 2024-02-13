def solution(inputArray):
    # Find the length of the longest strings
    max_length = max(len(s) for s in inputArray)
    
    # Filter the strings that have the maximum length
    longest_strings = [s for s in inputArray if len(s) == max_length]
    
    return longest_strings

