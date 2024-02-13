def solution(image):
    # Get the dimensions of the input image
    rows = len(image)
    cols = len(image[0])

    # Initialize the blurred image with zeros
    blurred_image = [[0] * (cols - 2) for _ in range(rows - 2)]

    # Iterate over the pixels in the blurred image
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Calculate the average value of the 3x3 square
            average_value = (image[i - 1][j - 1] + image[i - 1][j] + image[i - 1][j + 1] +
                             image[i][j - 1] + image[i][j] + image[i][j + 1] +
                             image[i + 1][j - 1] + image[i + 1][j] + image[i + 1][j + 1]) // 9

            # Assign the average value to the corresponding pixel in the blurred image
            blurred_image[i - 1][j - 1] = average_value

    return blurred_image

