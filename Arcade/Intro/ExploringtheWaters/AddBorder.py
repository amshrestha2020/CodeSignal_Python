def solution(picture):
    bordered_picture = ["*" * (len(picture[0]) + 2)]
    
    for row in picture:
        bordered_picture.append("*" + row + "*")
    
    bordered_picture.append("*" * (len(picture[0]) + 2))
    
    return bordered_picture

