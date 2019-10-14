"""
Task...

    Complete the method which accepts an array of integers, and returns one of the following:

Rules...

    "yes, ascending" - if the numbers in the array are sorted in an ascending order
    "yes, descending" - if the numbers in the array are sorted in a descending order
    "no" - otherwise

NOTE: You can assume the array will always be valid, and there will always be one correct answer.
"""
def is_sorted_and_how(arr):
    arr_sort = sorted(arr)
    arr_reverse = sorted(arr, reverse = True)
    #Compare array with the ascending sorted version of the array
    if(arr_sort == arr):
        return "yes, ascending"
    #else, compare the array with the descending sorted version of the array
    elif (arr_reverse == arr):
        return "yes, descending"
    return "no"


print(is_sorted_and_how([15, 7, 3, -8]))


"""
Created by...

    Jesus Lopez Mesia (https://www.linkedin.com/in/susejzepol/)

At date...
    
    2019-10-13
"""