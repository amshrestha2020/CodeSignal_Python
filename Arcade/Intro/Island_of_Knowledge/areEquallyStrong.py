def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    # Check if your strongest arm matches your friend's strongest arm
    strongest_match = (yourLeft == friendsLeft and yourRight == friendsRight) or (yourLeft == friendsRight and yourRight == friendsLeft)

    # Check if your weakest arm matches your friend's weakest arm
    weakest_match = (min(yourLeft, yourRight) == min(friendsLeft, friendsRight))

    # Return True if both strongest and weakest arms match, otherwise False
    return strongest_match and weakest_match

