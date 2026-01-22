def linear_search(array, value):  #Initialize a linear_search function with an array (the one we will use to search in) and a desired value whose index is to be found (x).
    for element in array: #Loop through every element in the array
        if element == value: #If and only if the element in each case is equal to the desired value...
            return array.index(value) #Return the index of that value in the array
    return -1 #The loop will only end if the search has failed. In this case it will return -1 (by convention we tend to return -1).

"""
A few words about linear search:

Linear search is a searching algorithm with an O(n) time complexity, meaning that the worst possible case is to take as many attempts to match an element
as the length of the array given to it. It searches of a given value x in a data structure (primarily an array), and it is a very simple and intuitive algorithm.



"""