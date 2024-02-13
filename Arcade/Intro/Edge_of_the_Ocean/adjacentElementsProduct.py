def solution(inputArray):
    max_product = float('-inf')

    # Iterate through the array, calculating the product of adjacent elements
    for i in range(len(inputArray) - 1):
        current_product = inputArray[i] * inputArray[i + 1]
        max_product = max(max_product, current_product)

    return max_product

