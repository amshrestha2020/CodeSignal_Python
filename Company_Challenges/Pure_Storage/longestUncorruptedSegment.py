def solution(sourceArray, destinationArray):
    max_length = 0
    max_start = 0
    current_length = 0
    current_start = 0

    for i in range(len(sourceArray)):
        if sourceArray[i] == destinationArray[i]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start = current_start
            current_length = 0
            current_start = i + 1

    if current_length > max_length:
        max_length = current_length
        max_start = current_start

    return [max_length, max_start]

# Test the function
sourceArray = [33531593, 96933415, 28506400, 39457872, 29684716, 86010806]
destinationArray = [33531593, 96913415, 28506400, 39457872, 29684716, 86010806]
print(solution(sourceArray, destinationArray))  # Output: [4, 2]
