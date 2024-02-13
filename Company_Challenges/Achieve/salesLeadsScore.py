def solution(names, time, netValue, isOnVacation):
    # Create a list of tuples containing name, score, time spent, and vacation status
    sales_leads = [(names[i], netValue[i] * time[i] / 365, time[i], isOnVacation[i]) for i in range(len(names))]

    # Filter out sales leads who are not on vacation
    sales_leads = [lead for lead in sales_leads if not lead[3]]

    # Sort sales leads based on score, time spent, and lexicographically smaller name
    sales_leads.sort(key=lambda x: (-x[1], -x[2], x[0]))

    # Extract names of sorted sales leads
    sorted_names = [lead[0] for lead in sales_leads]

    return sorted_names

# Test case
names = ["lead1", "lead2", "lead3", "lead4", "lead5"]
time = [250, 300, 250, 260, 310]
netValue = [1000, 800, 1100, 1200, 1000]
isOnVacation = [True, False, True, False, False]
print(solution(names, time, netValue, isOnVacation))  # Output: ["lead4", "lead5", "lead2"]
