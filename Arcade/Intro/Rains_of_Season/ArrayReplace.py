def solution(inputArray, elemToReplace, substitutionElem):
    # Use list comprehension to create a new array with replacements
    replaced_array = [substitutionElem if x == elemToReplace else x for x in inputArray]
    return replaced_array

