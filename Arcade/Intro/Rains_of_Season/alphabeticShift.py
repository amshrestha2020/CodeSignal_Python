def solution(inputString):
    result = ""
    for char in inputString:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                result += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            # Handle lowercase letters
            else:
                result += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        else:
            result += char
    return result

