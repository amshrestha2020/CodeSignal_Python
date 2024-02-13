def solution(inputString):
    abcCount = [0 for i in range(26)]
    for letter in inputString:
        abcCount[ord(letter) - 97] += 1
    for i in range(1, len(abcCount)):
        if abcCount[i] > abcCount[i - 1]:
            return False
    return True
