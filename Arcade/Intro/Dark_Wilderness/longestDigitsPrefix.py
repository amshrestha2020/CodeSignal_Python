def solution(inputString):
    longest_prefix = ""
    current_prefix = ""

    for char in inputString:
        if char.isdigit():
            current_prefix += char
        else:
            # Break the loop when a non-digit character is encountered
            break

        # Update the longest prefix if the current prefix is longer
        if len(current_prefix) > len(longest_prefix):
            longest_prefix = current_prefix

    return longest_prefix

