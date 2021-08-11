
'''
Sorting Algorithms

        1. Insertion Sort
        2. Quick Sort
        3. Bucket Sort
        4. Bubble Sort
        5. Merge Sort

Author: Isabella Doyle
'''

# Import modules
import random

# Implementation of Insertion Sort algorithm
# Ref: [1]
def insertionSort(arr):
    
    # Iterates over elements in the given array starting at index 2
    for i in range(1, len(arr)):
        j = i
        
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    
    return arr

# Implementations of Quick Sort algorithm               
# Ref: [2] !!!! CHANGE THIS ONE TO THE ONE HERE: https://brilliant.org/wiki/quick-sort/
def quickSort(arr):

    n = len(arr)
    
    if n < 2:           # Base case for recursion when the array contains one item
        return arr
    
    pivot = 0           # Position of partition

    # Partitioning loop
    for i in range(1, n): 
         if arr[i] <= arr[0]:
            pivot += 1
            temp = arr[i]
            arr[i] = arr[pivot]
            arr[pivot] = temp

    temp = arr[0]
    arr[0] = arr[pivot] 
    arr[pivot] = temp   # Places pivot in the correct position

    left = quickSort(arr[0:pivot]) # Sorts the items to the left of pivot
    right = quickSort(arr[pivot + 1: n]) # Sorts the items to the right of pivot
    arr = left + [arr[pivot]] + right # Combines the sorted items

    return arr

# Ref: [3]
# Implementation of Bucket Sort algorithm
def bucketSort(arr):
    
    # Finds biggest value in the array, using length of list to decide what value is placed into each bucket
    maximum = max(arr)
    size = maximum/len(arr)

    # Creates empty buckets corresponding with length of input list
    bucketList = []
    for x in range(len(arr)):
        bucketList.append([]) 

    # Places the items in the array into the appropriate bucket depending on its size
    for i in range(len(arr)):
        j = int (arr[i] / size)
        if j != len (arr):
            bucketList[j].append(arr[i])
        else:
            bucketList[len(arr) - 1].append(arr[i])

    # Sorts items in each bucket using the insertionSort function
    for z in range(len(arr)):
        insertionSort(bucketList[z])
            
    # Concatenates the sorted items from each bucket to form one sorted array
    final = []
    for x in range(len (arr)):
        final = final + bucketList[x]
    return final

# Implementation of Bubble Sort algorithm 
# Ref: [4]
def bubbleSort(arr):
    
    for i in range(len(arr)):
    
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

# Ref: [5]
# Implemetation of Merge Sort algorithm


# Generates an array of random numbers with a specified length
# Ref: [6]
amount = 20
arr = []
for i in range(0, amount):
    num = random.randint(1, 1000)
    arr.append(num)
print("Unsorted", arr)

print(bucketSort(arr))

'''
REFERENCES

[1] "Insertion Sort In Python Explained (With Example And Code)" by FelixTechTips. Available at: https://www.youtube.com/watch?v=R_wDA-PmGE4
[2] https://www.educative.io/edpresso/how-to-implement-quicksort-in-python 
[3] https://stackabuse.com/bucket-sort-in-python/
[4] Code adapted from https://stackabuse.com/bubble-sort-in-python
[5] 
[6] "Random - Generate pseudo-random numbers" https://docs.python.org/3/library/random.html

'''