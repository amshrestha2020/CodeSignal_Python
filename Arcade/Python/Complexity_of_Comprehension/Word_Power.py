def solution(word):
    num = {ch: ord(ch) - ord('a') + 1 for ch in 'abcdefghijklmnopqrstuvwxyz'}
    return sum([num[ch] for ch in word])
