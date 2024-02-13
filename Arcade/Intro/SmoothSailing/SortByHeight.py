def solution(a):
    # Extract the heights of people from the array
    heights = [h for h in a if h != -1]
    
    # Sort the heights in non-descending order
    sorted_heights = sorted(heights)
    
    # Create an iterator for the sorted heights
    height_iterator = iter(sorted_heights)
    
    # Replace non-tree elements in the original array with sorted heights
    result = [next(height_iterator) if elem != -1 else -1 for elem in a]
    
    return result

