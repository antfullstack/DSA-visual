def interpolation_search(array, target):
    high = len(array) - 1 #The upper bound of the array (the last index or length -1 due to zero-based indexing initially)
    low = 0 #The lower bound, initially 0 
    while high >= low: #While low does not surpass high and high does not go lower than low...
        key =  ((target + array[low]) + (high - low)) // (array[high] - array[low]) #Equation below
        if array[key] == target: #If the array element at the position of the middle is equal to our target...
            return key #return the index of the middle which is of course equal to the element's index.
        
        if array[key] < target: #If the value of array[middle] is lower than target...
            low = key + 1 #make the lower bound go to were the middle was previously plus 1
        
        if array[key] > target: #If the value of array[middle] is higher than target...
            high = key - 1 #make the lower bound go to were the middle was previously minus 1
    return -1 #If the function has not returned anything and the loop has managed to end, basically no element was found, so return -1.


"""
Interpolation search is like the older cousin of binary search. The same O(log n) complexity, check conditions and loops as well
as return values but with a different equation. 

They key equation that predicts the key used at each iteration is described as: 
    ((target + array[low]) + (high - low)) // (array[high] - array[low]) 

This is the fundamental principle of interpolation search and it requireds a uniformly ordered array. 
NOTE: Interpolation search does NOT calculate a middle, but rather a prediction point. So, in contrast to binary search, 
it would be innacurate to name the constantly recalculated variable "middle". In this example, the name "key" is present. 
"""