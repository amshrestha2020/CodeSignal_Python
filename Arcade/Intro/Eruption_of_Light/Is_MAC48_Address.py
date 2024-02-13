import re

def solution(inputString):
    mac_pattern = re.compile(r'^([0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}$')
    return bool(mac_pattern.match(inputString))