def solution(s1, s2):
    # Convert strings to lists for easier manipulation
    list1 = list(s1)
    list2 = list(s2)
    
    common_count = 0
    
    # Iterate through the characters of the first string
    for char in s1:
        # Check if the character is present in both strings
        if char in list2:
            # Increment the common count
            common_count += 1
            # Remove the character from the second string to avoid duplicates
            list2.remove(char)
    
    return common_count

