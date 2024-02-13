def solution(inputString):
    char_count = {}
    
    # Count the occurrences of each character
    for char in inputString:
        char_count[char] = char_count.get(char, 0) + 1

    # Count the number of characters with odd occurrences
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    # For a palindrome, at most one character can have an odd count
    return odd_count <= 1

