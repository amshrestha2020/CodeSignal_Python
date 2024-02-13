def solution(n):
    # Convert the integer to a string to iterate through its digits
    str_n = str(n)
    
    # Check if all digits are even
    return all(int(digit) % 2 == 0 for digit in str_n)

