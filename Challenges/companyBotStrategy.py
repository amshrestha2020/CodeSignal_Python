def solution(trainingData):
    correct_times = [data[0] for data in trainingData if data[1] == 1]
    if not correct_times:
        return 0.0
    return sum(correct_times) / len(correct_times)
