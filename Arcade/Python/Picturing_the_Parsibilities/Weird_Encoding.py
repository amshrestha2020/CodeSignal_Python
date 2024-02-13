import base64

def solution(encoding, message):
    # Create a translation table
    trans = str.maketrans(encoding, '+/')

    # Translate the message
    message = message.translate(trans)

    # Decode the message
    message = base64.b64decode(message).decode()

    return message
