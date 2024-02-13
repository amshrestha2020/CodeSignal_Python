def solution(n):
    # Convert the ticket number to a string
    ticket_str = str(n)
    
    # Calculate the length of the first half
    half_length = len(ticket_str) // 2
    
    # Split the string into two halves
    first_half = ticket_str[:half_length]
    second_half = ticket_str[half_length:]
    
    # Calculate the sum of digits in each half
    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)
    
    # Check if the sums are equal
    return sum_first_half == sum_second_half

