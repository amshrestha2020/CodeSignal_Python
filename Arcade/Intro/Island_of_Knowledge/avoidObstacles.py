def solution(inputArray):
    max_obstacle = max(inputArray)
    
    for jump_length in range(1, max_obstacle + 2):
        can_jump = all((x % jump_length != 0) for x in inputArray)
        if can_jump:
            return jump_length

