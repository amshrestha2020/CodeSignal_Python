def solution(names):
    seen_names = {}
    result = []

    for name in names:
        if name not in seen_names:
            seen_names[name] = 1
            result.append(name)
        else:
            new_name = f"{name}({seen_names[name]})"
            while new_name in seen_names:
                seen_names[name] += 1
                new_name = f"{name}({seen_names[name]})"
            
            seen_names[new_name] = 1
            result.append(new_name)

    return result

