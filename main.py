
'''
Sorting Algorithms

        1. Insertion Sort
        2. Quick Sort
        3. Bucket Sort
        4. Bubble Sort
        5. Merge Sort

Author: Isabella Doyle
'''

# Imports modules
import time
import random
import numpy as np
import pandas as pd

# Implementation of Insertion Sort algorithm | Ref: [1]
def insertionSort(arr):
    
    # Iterates over elements in the given arr starting at index 2
    for i in range(1, len(arr)):
        
        while arr[i - 1] > arr[i] and i > 0:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1  # Moves down one index
    
    return arr

# Implementations of Quick Sort algorithm | Ref: [2]            
# !!!! CHANGE THIS ONE TO THE ONE HERE: https://brilliant.org/wiki/quick-sort/
def quickSort(arr):

    n = len(arr)
    
    if n < 2:           # Base case for recursion when the arr contains one item
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

# Implementation of Bucket Sort algorithm | Ref: [3]
def bucketSort(arr):
    
    # Finds biggest value in the arr, using length of list to decide what value is placed into each bucket
    maximum = max(arr)
    size = maximum/len(arr)

    # Creates empty buckets corresponding with length of input list
    bucketList = []
    for x in range(len(arr)):
        bucketList.append([]) 

    # Places the items in the arr into the appropriate bucket depending on its size
    for i in range(len(arr)):
        i = int (arr[i] / size)
        if i != len (arr):
            bucketList[i].append(arr[i])
        else:
            bucketList[len(arr) - 1].append(arr[i])

    # Sorts items in each bucket using the insertionSort() function
    for z in range(len(arr)):
        insertionSort(bucketList[z])
            
    # Concatenates the sorted items from each bucket to form one sorted arr
    final = []
    for x in range(len (arr)):
        final = final + bucketList[x]
    return final

# Implementation of Bubble Sort algorithm | Ref: [4]
def bubbleSort(arr):
    
    for i in range(len(arr)):
    
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr

# Function called in mergeSort() to merge arrays | Ref: 5
# This part of the mergeSort alogrithm carries out the actual 
# sorting of the elements in the array
def merge(left, right): # Takes in two lists from the mergeSort() function
    
    # If left arr is empty return right
    if len(left) == 0:
        return right

    # If second is empty return left arr
    if len(right) == 0:
        return left

    result = []     # Empty list that stores result of merge
    indexLeft = 0   # Pointers 
    indexRight = 0  

    
    while len(result) < len(left) + len(right):
        

        if left[indexLeft] <= right[indexRight]:
            result.append(left[indexLeft])
            indexLeft += 1
        else:
            result.append(right[indexRight])
            indexRight += 1

        # If you reach the end of either arr, then you can
        # add the remaining elements from the other arr to
        # the result and break the loop
        if indexRight == len(right):
            result += left[indexLeft:]
            break

        if indexLeft == len(left):
            result += right[indexRight:]
            break

    return result

# Implemetation of Merge Sort algorithm | Ref: [5]
# This part of the merge sort algorithm uses the 'divide and conquer' method
def mergeSort(arr):
    
    # Base case if array has less than 2 items
    if len(arr) < 2:
        return arr

    midpoint = len(arr) // 2    # Identifies midpoint of array

    # Using recursion the partitioned portions of the array are 
    # broken down until they are individual components, after being
    # re-organised with mergeSort() function, two arrays (left and right) 
    # are returned and merged together to create a final sorted list
    return merge(
        left = mergeSort(arr[:midpoint]),
        right = mergeSort(arr[midpoint:]))

'''
Benchmarking for sorting algorithms
'''

# Generates an array of random numbers with parameters for size & min/max values
def genRandomArr(n=10, min=1, max=1000):
    # Creates empty array
    arr = []
    # Creates random numbers n times & appends them to 'arr'
    for i in range(0, n):
        num = random.randint(min, max)
        arr.append(num)
    # Returns array to caller
    return arr

# Times algorithm
def timeAlgo(algo, arr):
    # Starts timing
    start = time.time()
    # Executes algorithm
    algo(arr)
    # Ends timing
    end = time.time()
    totalTime = end - start
    return totalTime

# Main program
def main():



# Executes the code 10X and returns how long each exectution took p/s

'''
REFERENCES

[1] "Insertion Sort In Python Explained (With Example And Code)" by FelixTechTips. Available at: https://www.youtube.com/watch?v=R_wDA-PmGE4
[2] https://www.educative.io/edpresso/how-to-implement-quicksort-in-python 
[3] https://stackabuse.com/bucket-sort-in-python/
[4] Code adapted from https://stackabuse.com/bubble-sort-in-python
[5] https://realpython.com/sorting-algorithms-python/
[6] "Random - Generate pseudo-random numbers" https://docs.python.org/3/library/random.html

'''

### THIS FOR BENCHMARKING AND EVERYTHING: https://realpython.com/sorting-algorithms-python/