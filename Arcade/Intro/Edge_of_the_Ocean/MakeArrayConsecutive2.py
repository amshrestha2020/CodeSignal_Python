def solution(statues):
    if not statues:
        return 0

    min_statue = min(statues)
    max_statue = max(statues)

    required_range = range(min_statue, max_statue + 1)

    missing_statues = [value for value in required_range if value not in statues]

    return len(missing_statues)

