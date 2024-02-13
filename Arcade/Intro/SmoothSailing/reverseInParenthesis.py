def solution(inputString):
    stack = []
    result = list(inputString)
    
    for i, char in enumerate(inputString):
        if char == '(':
            stack.append(i)
        elif char == ')':
            start = stack.pop()
            result[start+1:i] = reversed(result[start+1:i])
    
    # Remove parentheses from the final result
    result = [char for char in result if char not in '()']
    
    return ''.join(result)
