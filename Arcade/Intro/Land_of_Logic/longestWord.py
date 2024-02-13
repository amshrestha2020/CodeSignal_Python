import re

def solution(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    longest_word = max(words, key=len, default="")
    return longest_word

