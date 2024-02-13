def solution(code):
    # Split the code into 8-bit chunks
    chunks = [code[i:i+8] for i in range(0, len(code), 8)]

    # Convert each chunk to its decimal representation and then to a character
    decoded_message = ''.join([chr(int(chunk, 2)) for chunk in chunks])

    return decoded_message

