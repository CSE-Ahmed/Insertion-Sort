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


# Main function to test the insertion sort implementation
N = 50
data = random.sample(range(1, 1001), N)  # Generate a list of N unique random integers between 1 and 1000

print("Before sortng:") # Print the original unsorted list
print(data)

start = time.perf_counter() # Start the timer for performance measurement
comparisons, shifts = insertion_sort(data)
end = time.perf_counter()

print("\nAfter sorting:")
print(data)
print("\nComparisons:", comparisons)
print("Shifts:", shifts)
print(f"Time: {end - start:.6f} seconds")
print("Sorted correctly?", data == sorted(data))