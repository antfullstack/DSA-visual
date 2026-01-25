def binary_search(array, target): #Binary search function takes an array and a value whose index is to be found.
    high = len(array) - 1 #The upper bound of the array (the last index or length -1 due to zero-based indexing initially)
    low = 0 #The lower bound, initially 0 
    while high >= low: #While low does not surpass high and high does not go lower than low...
        middle =  low + (high + low) // 2 #Calculate the middle to be low plus the sum of high + low dvided by 2 (rounded to lowest integer)
        if array[middle] == target: #If the array element at the position of the middle is equal to our target...
            return middle #return the index of the middle which is of course equal to the element's index.
        
        if array[middle] < target: #If the value of array[middle] is lower than target...
            low = middle + 1 #make the lower bound go to were the middle was previously plus 1
        
        if array[middle] > target: #If the value of array[middle] is higher than target...
            high = middle - 1 #make the lower bound go to were the middle was previously minus 1
    return -1 #If the function has not returned anything and the loop has managed to end, basically no element was found, so return -1.

"""
A few words about binary search: 

Binary search is an important searching algorithm in computer science with a O(log n) complexity. Trough every iteration, 
if the target is not found, it excludes half of the array. Think of it like a phonebook. Let's say you want to call a 
person named Jane. If you are on letter M (the middle), your letter is in a letter before M, so you will have to lower
the upper bound to middle - 1, essentially halving this instance, and if the value is stil not found, halve this instance
e.t.c...

(The same would happen if we looked for a letter after M. For example, if we looked for J this would make the upper bound equal to middle plus 1)
(The middle is recalculated through the start of every iteration, that is why we only change the variables low and high. It is basically a functon itself...)

TIP: Implement this with a small array on a pen and paper.
"""