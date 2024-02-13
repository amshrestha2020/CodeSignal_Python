def solution(inputString):
    for char in inputString:
        if char.isdigit():
            return char
    return None 

