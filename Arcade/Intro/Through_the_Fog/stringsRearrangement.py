def difference_by_one(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1

def is_valid_path(path, graph):
    for i in range(1, len(path)):
        if path[i] not in graph[path[i - 1]]:
            return False
    return True

def solution(inputArray):
    n = len(inputArray)

    # Build the graph based on the difference by one character
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if difference_by_one(inputArray[i], inputArray[j]):
                graph[i].append(j)
                graph[j].append(i)

    # Backtracking to check all possible arrangements
    def backtrack(path):
        if len(path) == n:
            return is_valid_path(path, graph)

        for node in graph[path[-1]]:
            if node not in path:
                path.append(node)
                if backtrack(path):
                    return True
                path.pop()

        return False

    # Try all possible starting nodes
    for start_node in range(n):
        if backtrack([start_node]):
            return True

    return False

