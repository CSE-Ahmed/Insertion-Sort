import time
import random 

def insertion_sort(arr):
    Comparisons = 0 # number of comparisons
    shifts = 0      # number of shifts


    # loop through each element in the array starting from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1 

        # while loop to find the correct position for the key
        while j >= 0 :
           Comparisons += 1

           if arr[j] > key:
               arr[j + 1] = arr[j] # Shift the element to the right
               shifts += 1
               j -= 1

           else:break
              
        arr[j + 1] = key

    return Comparisons, shifts
