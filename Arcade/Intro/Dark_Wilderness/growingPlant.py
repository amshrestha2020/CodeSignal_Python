def solution(upSpeed, downSpeed, desiredHeight):
    current_height = 0
    day_count = 0

    while current_height < desiredHeight:
        day_count += 1
        current_height += upSpeed

        if current_height >= desiredHeight:
            break

        current_height -= downSpeed

    return day_count

