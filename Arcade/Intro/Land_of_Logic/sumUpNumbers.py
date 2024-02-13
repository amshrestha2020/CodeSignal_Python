import re

def solution(inputString):
    numbers = re.findall(r'\d+', inputString)
    
    # Convert the numbers from strings to integers and calculate the sum
    total_sum = sum(map(int, numbers))
    
    return total_sum

