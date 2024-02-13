def solution(inputArray):
    moves = 0
    prev = inputArray[0]

    for num in inputArray[1:]:
        if num <= prev:
            moves += prev - num + 1
            prev += 1
        else:
            prev = num

    return moves

