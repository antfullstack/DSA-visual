def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j+1],array[j] = array[j+1],array[j]
    return array

"""
Bubble sort is a sorting algorithm with a O(n**2) (n squared) time complexity. It involves a loop who runs as many times as the length of the array.
An inner loop is nested into it, which everytime runs length - outer loop value - 1 times. That loop checks for a condition. That is, if the value at the index
of the value of the loop at this given time is larger to the value of the next element (index+1) in the array. If that's the case, the values are swapped so the array 
is closer to sorting. 

Why j - i - 1? Well, in order to not go through the already sorted. It would be reccomended to visualize this in pen and paper, or you can also see it through the visuals.
"""