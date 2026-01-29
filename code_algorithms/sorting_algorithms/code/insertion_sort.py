def insertion_sort(array):
    n = len(array)

    for key in range(1, n): #Run from index one to the number of the last index (assuming the first element belongs in the sorted part).
        index = key #We define a temporary index over each iteration

        while array[index-1] > array[index] and index > 0:  #While the previous element of the array[index] is larger than the array[index] itself...
            array[index-1],array[index] = array[index],array[index-1] #swap the previous and the current index in the array 
            index -= 1 #reduce index by 1

"""
Insertion sort has an O(n*n) complexity. 

How it works is that starting from the leftmost index + 1 (so index 1), assuming index 0 is sorted, and ending at the last index, it creates a sorted and an unsorted part
and constantly expands the sorted part with the following operation: 
    Define a temporary index:
        If this temporary index has its previous element be larger than it, swap their places. 
        Do this while the latter is true, and while the index is greater than 0.

    This process basically assumes that the sorted part is fully sorted (it is), and adds the first element of the unsorted part to it with each iteration.
    It does this by placing it in the correct place, either leaving it alone if it is the largest in value element, or constantly swapping it until: prev =< element =< next (sorted). 
"""
