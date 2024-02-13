def solution(address):
    # Split the email address into local and domain parts
    parts = address.split('@')

    # Return the domain part
    return parts[-1]

